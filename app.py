import streamlit as st
from google import genai
from google.genai import types

# ==========================================
# 1. IDENTIDAD VISUAL Y CONFIGURACIÓN
# ==========================================
st.set_page_config(
    page_title="SYLLATERAL AI | Inteligencia Cívica",
    page_icon="🏛️",
    layout="wide"
)

# Estilos visuales (Naranja Terracota, Negro Cerámica, Pergamino)
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #F7F5F0; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { color: #D96B27 !important; font-family: 'Montserrat', sans-serif; }
    .st-chat-message-user { background-color: #1E1E1E !important; border-left: 3px solid #EED3A1; }
    .st-chat-message-assistant { background-color: #121212 !important; border-left: 3px solid #D96B27; }
    .database-box { background-color: #1E1E1E; padding: 15px; border-radius: 8px; border: 1px solid #D96B27; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CONTEXTO CÍVICO Y BASES DE DATOS
# ==========================================
DATOS_ABIERTOS = """
- Presupuesto participativo promedio para proyectos juveniles: $15,000 - $50,000 USD.
- Indicador local: 65% de los espacios públicos y parques necesitan rehabilitación de luminarias.
- Tasa de deserción en actividades extracurriculares por falta de transporte: 22%.
"""

DIAGNOSTICOS_CIUDADANOS = """
- Petición #402: "Necesitamos espacios seguros para el arte y teatro en las tardes."
- Petición #405: "Falta de integración entre adultos mayores y jóvenes en actividades comunitarias."
- Petición #410: "Las calles aledañas a los colegios son inseguras por falta de señalización."
"""

ESTRUCTURAS_ORATORIA = """
Regla de los 2 Minutos (Máximo 300 palabras):
1. Exordio (Gancho): Una pregunta o estadística impactante (15 seg).
2. Narratio (El Problema): Explicación del diagnóstico ciudadano validado con datos (30 seg).
3. Propositio (La Solución): La idea lateral innovadora, explicando su viabilidad presupuestaria (45 seg).
4. Peroratio (Cierre): Llamado a la acción que apele a la emoción ciudadana (30 seg).
"""

# ==========================================
# 3. PROMPT MAESTRO AMPLIO (CONEXIÓN WEB)
# ==========================================
INSTRUCCION_SISTEMA = f"""
Eres el Asistente de Inteligencia Cívica y Estrategia Cívico-Académica de SYLLATERAL AI.
Tu objetivo es actuar como un consultor de alto nivel experto en desarrollo sostenible, innovación social, tecnología, oratoria y debate.

TUS EJES FUNDAMENTALES DE CONOCIMIENTO:
1. DESARROLLO SOSTENIBLE, SOCIAL Y TECNOLÓGICO:
   - Objetivos de Desarrollo Sostenible (ODS), políticas públicas, innovación ciudadana y tecnologías cívicas (CivicTech).
2. ORATORIA, PERSUASIÓN Y DEBATE ABIERTO:
   - Retórica clásica y moderna, construcción de discursos de alto impacto, estrategia de debate y técnicas de persuasión.
3. FUENTES OFICIALES Y ACADÉMICAS EN ESPAÑOL:
   - Integración de ensayos, artículos académicos, conferencias, libros digitales, cifras de organismos oficiales e investigaciones recientes.
   - Uso impecable, elocuente y bien fundamentado del idioma español.

DATOS Y CONTEXTO LOCAL DE APOYO:
[DATOS ABIERTOS]: {DATOS_ABIERTOS}
[DIAGNÓSTICOS CIUDADANOS]: {DIAGNOSTICOS_CIUDADANOS}
[ESTRUCTURA DE ORATORIA]: {ESTRUCTURAS_ORATORIA}

PAUTAS DE RESPUESTA:
- Utiliza la información de internet en tiempo real para respaldar tus argumentos con datos precisos, citas de conferencias, artículos o marcos oficiales.
- Mantén un tono motivador, riguroso, persuasivo y conversacional.
- Ayuda al usuario a estructurar propuestas comunitarias, debates sólidos y discursos elocuentes.
"""

# ==========================================
# 4. INTERFAZ DE USUARIO Y PANEL LATERAL
# ==========================================
st.title("🏛️ SYLLATERAL AI")
st.markdown("*La información nace, crece, se reproduce pero no debe morir.*")

with st.sidebar:
    st.header("Flujo de Inteligencia Cívica")
    st.markdown("Monitor de conexión con las bases de datos del sistema:")
    st.markdown("<div class='database-box'>🌐 <b>Búsqueda Web en Vivo</b><br><i>Google Search Grounding activo</i></div>", unsafe_allow_html=True)
    st.markdown("<div class='database-box'>🌱 <b>Desarrollo & ODS</b><br><i>Fuentes oficiales y sostenibilidad</i></div>", unsafe_allow_html=True)
    st.markdown("<div class='database-box'>🏛️ <b>Oratoria & Debate</b><br><i>Persuasión y retórica activa</i></div>", unsafe_allow_html=True)

    api_key = st.text_input("🔑 API Key de Gemini:", type="password")

if not api_key:
    st.warning("Introduce tu API Key en el panel lateral para arrancar el motor de Inteligencia Cívica.")
    st.stop()

# Historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Bienvenido a **SYLLATERAL AI**! Mi motor está conectado en tiempo real a fuentes web oficiales, artículos, ensayos, marcos de desarrollo sostenible y retórica. ¿Qué tema, debate o propuesta deseas analizar hoy?"}
    ]

# Renderizar historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada de usuario
if user_input := st.chat_input("Escribe tu idea, consulta, propuesta o debate..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Investigando en tiempo real y construyendo respuesta..."):
            try:
                client = genai.Client(api_key=api_key.strip())

                # Formatear historial para Gemini
                history_contents = []
                for m in st.session_state.messages:
                    role = "user" if m["role"] == "user" else "model"
                    history_contents.append({
                        "role": role,
                        "parts": [{"text": m["content"]}]
                    })

                # Generar contenido activando Google Search Grounding
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=history_contents,
                    config=types.GenerateContentConfig(
                        system_instruction=INSTRUCCION_SISTEMA,
                        temperature=0.7,
                        tools=[{"google_search": {}}]  # Búsqueda en vivo en internet
                    )
                )

                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

            except Exception as e:
                st.error(f"❌ Error al consultar la API: {e}")
