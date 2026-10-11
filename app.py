import streamlit as st
from google import genai
from google.genai import types

# ==========================================
# 1. CONFIGURACIÓN E IDENTIDAD VISUAL
# ==========================================
st.set_page_config(
    page_title="SYLLATERAL AI | Plataforma Cívica",
    page_icon="🏛️",
    layout="wide"
)

# Estilos CSS con la paleta visual oficial (Terracota, Negro Cerámica, Pergamino, Blanco)
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #F7F5F0; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { color: #D96B27 !important; font-family: 'Montserrat', sans-serif; }
    .st-chat-message-user { background-color: #1E1E1E !important; border-left: 3px solid #EED3A1; }
    .st-chat-message-assistant { background-color: #121212 !important; border-left: 3px solid #D96B27; }
    .database-box { background-color: #1E1E1E; padding: 15px; border-radius: 8px; border: 1px solid #D96B27; margin-bottom: 10px; }
    .quote-box { background-color: #1E1E1E; border-left: 4px solid #D96B27; padding: 15px; margin: 20px 0; border-radius: 4px; }
    .card-step { background-color: #1E1E1E; border: 1px solid #333; padding: 20px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Contexto cívico predeterminado
DATOS_ABIERTOS = "- Presupuesto participativo juvenil: $15,000 - $50,000 USD.\n- 65% de espacios públicos requieren luminarias.\n- 22% deserción por transporte."
DIAGNOSTICOS_CIUDADANOS = "- Petición #402: Espacios seguros para arte y teatro.\n- Petición #405: Integración adultos mayores y jóvenes.\n- Petición #410: Inseguridad vial escolar."
ESTRUCTURAS_ORATORIA = "Regla de los 2 Minutos: Exordio (15s), Narratio (30s), Propositio (45s), Peroratio (30s)."

INSTRUCCION_SISTEMA = f"""
Eres el Asistente de Inteligencia Cívica y Estrategia Cívico-Académica de SYLLATERAL AI.
Tu objetivo es actuar como un consultor político, cívico y retórico de alto nivel, experto en desarrollo sostenible, innovación social, tecnología, oratoria y debate.
DATOS Y CONTEXTO:
[DATOS ABIERTOS]: {DATOS_ABIERTOS}
[DIAGNÓSTICOS CIUDADANOS]: {DIAGNOSTICOS_CIUDADANOS}
[ESTRUCTURA DE ORATORIA]: {ESTRUCTURAS_ORATORIA}
Pautas: Sé motivador, firme, elocuente y conversacional. Ayuda a estructurar propuestas comunitarias y discursos persuasivos de 2 minutos.
"""

# ==========================================
# 2. MENÚ DE NAVEGACIÓN LATERAL
# ==========================================
with st.sidebar:
    st.title("🏛️ SYLLATERAL AI")
    st.markdown("*Inteligencia Cívica & Oratoria*")
    st.markdown("---")
    
    seccion = st.radio(
        "📌 Navegación del Sistema:",
        ["1. Inicio / Caso de Estudio", "2. Chatbot Cívico", "3. Entrenador de Oratoria"],
        index=0
    )
    
    st.markdown("---")
    if seccion == "2. Chatbot Cívico":
        st.subheader("🔑 Autenticación")
        api_key = st.text_input("Ingresa tu API Key de Gemini:", type="password")
    else:
        api_key = None

# ==========================================
# SECCIÓN 1: INICIO / CASO DE ESTUDIO
# ==========================================
if seccion == "1. Inicio / Caso de Estudio":
    st.title("🏛️ SYLLATERAL AI")
    st.subheader("Inteligencia Cívica, Creatividad y Oratoria para Transformar Nuestra Comunidad")
    
    st.markdown("""
    <div class='quote-box'>
        <h3>"La información nace, crece, se reproduce pero no debe morir."</h3>
        <p><i>— Sherlyn Stapf</i></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 1. Visión del Proyecto")
        st.write("""
        Hoy vivimos rodeados de más información que nunca, pero muchas decisiones públicas y proyectos comunitarios siguen siendo burocráticos y repetitivos. 
        **SYLLATERAL AI** une la tecnología del siglo XXI con la fuerza de la filosofía y la oratoria clásica.
        
        Pasamos de acumular datos en carpetas a inspirar a los líderes comunitarios, enseñándoles a idear soluciones innovadoras y a defenderlas con pasión.
        """)
        
        st.markdown("### 2. El Problema: Tres Fallas")
        st.markdown("""
        * **📁 Información:** Investigaciones valiosas terminan archivadas en carpetas digitales.
        * **💡 Soluciones:** Propuestas repetitivas desconectadas de las necesidades reales.
        * **🗣️ Discursos:** Excelentes proyectos técnicos fracasan porque sus líderes no saben explicarlos ni defenderlos en público.
        """)

    with col2:
        st.markdown("### 3. Los Dos Pilares del Pensamiento")
        st.markdown("""
        * **Pensamiento Lateral (Edward de Bono):** *Crear el camino.* Rompemos el molde tradicional para imaginar ideas innovadoras y distintas.
        * **Lógica Deductiva (Aristóteles):** *Comprobar el camino.* Evaluamos cada idea con datos reales para garantizar que sea 100% realizable.
        """)
        
        st.markdown("<div class='database-box'><b>📊 Data Integrada al Sistema:</b><br>• Datos Abiertos y Presupuestos<br>• Diagnósticos Ciudadanos Activos<br>• Algoritmos de Retórica Clásica</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 4. Metodología en 3 Pasos")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card-step'><h4>01. Generación</h4><p>Análisis contextual y pensamiento lateral para crear ideas fuera de lo común.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-step'><h4>02. Validación</h4><p>Evaluación deductiva con evidencia real para asegurar viabilidad técnica y económica.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-step'><h4>03. Oratoria</h4><p>Simulación de debates y ensayos para lograr discursos sintéticos y persuasivos (2 min).</p></div>", unsafe_allow_html=True)

# ==========================================
# SECCIÓN 2: CHATBOT CÍVICO
# ==========================================
elif seccion == "2. Chatbot Cívico":
    st.title("💬 Asistente de Inteligencia Cívica")
    st.markdown("Interactive System for Community Leadership & Strategic Speechwriting.")

    if not api_key:
        st.warning("⚠️ Ingresa tu API Key de Gemini en el panel lateral izquierdo para activar el motor conversacional.")
        st.stop()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Bienvenido a **SYLLATERAL AI**! Soy tu consultor de Inteligencia Cívica, oratoria y liderazgo. ¿Qué debate, propuesta o problemática comunitaria deseas abordar hoy?"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_input := st.chat_input("Escribe tu idea, consulta o propuesta..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Procesando consulta..."):
                try:
                    client = genai.Client(api_key=api_key.strip())
                    history_contents = []
                    for m in st.session_state.messages:
                        role = "user" if m["role"] == "user" else "model"
                        history_contents.append({"role": role, "parts": [{"text": m["content"]}]})

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=history_contents,
                        config=types.GenerateContentConfig(
                            system_instruction=INSTRUCCION_SISTEMA,
                            temperature=0.7,
                        )
                    )
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"❌ Error de conexión: {e}")

# ==========================================
# SECCIÓN 3: ENTRENADOR DE ORATORIA
# ==========================================
elif seccion == "3. Entrenador de Oratoria":
    st.title("👁️ Módulo de Lenguaje Corporal & Presencia Escénica")
    st.markdown("Evaluación visual en tiempo real entrenada con **Google Teachable Machine**.")

    st.markdown("---")
    
    st.write("""
    Este módulo utiliza visión por computadora para analizar tu postura, contacto visual y gestos faciales durante la práctica de tu discurso de 2 minutos.
    """)

    st.info("💡 **Instrucciones:** Permite el acceso a tu cámara cuando se solicite para interactuar con tu modelo de Machine Learning.")

    # Enlace directo por si el navegador bloquea el iframe de la cámara
    st.markdown("[🔗 Abrir Entrenador de Teachable Machine en Pantalla Completa](https://teachablemachine.withgoogle.com/models/goHC2RCen/)")
    
    st.markdown("---")

    # Integración del modelo mediante iframe embebido
    st.components.v1.iframe("https://teachablemachine.withgoogle.com/models/goHC2RCen/", height=650, scrolling=True)
