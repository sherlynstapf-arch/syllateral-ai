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

# Estilos con los colores del anteproyecto: Naranja Terracota, Negro Cerámica y Pergamino
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
# 2. BASES DE DATOS Y CONTEXTO CÍVICO
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
# 3. PROMPT MAESTRO DEL CONSULTOR CÍVICO
# ==========================================
INSTRUCCION_SISTEMA = f"""
Eres el Asistente de Inteligencia Cívica de SYLLATERAL AI.
Tu objetivo es actuar como un consultor político, cívico y retórico altamente fluido, receptivo y estratégico.

TUS ÁREAS DE ESPECIALIDAD:
- Inteligencia Cívica y Liderazgo Comunitario.
- Debates Abiertos, Análisis Crítico e Innovación Pública (Pensamiento Lateral).
- Diagnósticos Cívicos y Solución de Problemáticas Sociales.
- Oratoria Clásica, Redacción de Discursos y Técnicas de Persuasión.

DATOS Y CONTEXTO DE APOYO:
[DATOS ABIERTOS]: {DATOS_ABIERTOS}
[DIAGNÓSTICOS CIUDADANOS]: {DIAGNOSTICOS_CIUDADANOS}
[ESTRUCTURA DE ORATORIA]: {ESTRUCTURAS_ORATORIA}

PAUTAS CONVERSACIONALES:
1. Mantén un diálogo 100% conversacional, natural y dinámico. Responde de forma directa a lo que el usuario plantee.
2. Si el usuario hace una pregunta general de debate o liderazgo, respóndela con criterio estratégico.
3. Si plantea una propuesta comunitaria, ayúdale a refinarla aplicando pensamiento lateral, validándola con datos reales y creando discursos persuasivos.
4. Tu tono es motivador, firme, elocuente y profesional.
"""

# ==========================================
# 4. INTERFAZ Y CHATBOT
# ==========================================
st.title("🏛️ SYLLATERAL AI")
st.markdown("*La información nace, crece, se reproduce pero no debe morir.*")

# Panel Lateral
with st.sidebar:
    st.header("Flujo de Inteligencia Cívica")
    st.markdown("Monitor de conexión con las bases de datos del sistema:")
    st.markdown("<div class='database-box'>📊 <b>Datos Abiertos</b><br><i>Conectado a métricas y presupuesto</i></div>", unsafe_allow_html=True)
    st.markdown("<div class='database-box'>🗣️ <b>Diagnósticos</b><br><i>Peticiones ciudadanas activas</i></div>", unsafe_allow_html=True)
    st.markdown("<div class='database-box'>🏛️ <b>Oratoria Clásica</b><br><i>Algoritmo de retórica activo</i></div>", unsafe_allow_html=True)

    api_key = st.text_input("🔑 API Key de Gemini:", type="password")

if not api_key:
    st.warning("Introduce tu API Key en el panel lateral para arrancar el motor de Inteligencia Cívica.")
    st.stop()

# Historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Bienvenido a **SYLLATERAL AI**. Soy tu consultor de Inteligencia Cívica, oratoria y liderazgo. ¿Qué debate, propuesta o problemática comunitaria deseas abordar hoy?"}
    ]

# Renderizar mensajes anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Captura de input del usuario
if user_input := st.chat_input("Escribe tu idea, consulta, propuesta o debate..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generar respuesta
    with st.chat_message("assistant"):
        with st.spinner("Analizando respuesta..."):
            try:
                client = genai.Client(api_key=api_key)

                # Convertir historial al formato requerido por el SDK
                formatted_contents = []
                for m in st.session_state.messages:
                    role = "user" if m["role"] == "user" else "model"
                    formatted_contents.append(
                        types.Content(
                            role=role,
                            parts=[types.Part.from_text(text=m["content"])]
                        )
                    )

                # Generación fluida de respuesta
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=formatted_contents,
                    config=types.GenerateContentConfig(
                        system_instruction=INSTRUCCION_SISTEMA,
                        temperature=0.7,
                    )
                )

                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

            except Exception as e:
                st.error(f"Error en la respuesta: {e}")
