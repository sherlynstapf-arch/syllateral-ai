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

# Aplicando los colores del anteproyecto: Naranja Terracota, Negro Cerámica, Pergamino Cálido, Blanco Cerámico
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
# 2. BASES DE DATOS SIMULADAS (Contexto)
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
# 3. CONSTRUCCIÓN DEL PROMPT MAESTRO
# ==========================================
INSTRUCCION_SISTEMA = f"""
Eres el Asistente de Inteligencia Cívica de SYLLATERAL AI. Tu objetivo es acabar con la burocracia aburrida y crear proyectos comunitarios viables y persuasivos.
Nunca hables de forma genérica. Actúa como un consultor político y cívico exigente.

TIENES ACCESO A LA SIGUIENTE DATA PARA VALIDAR PROYECTOS:
[DATOS ABIERTOS Y ESTADÍSTICAS]: {DATOS_ABIERTOS}
[DIAGNÓSTICOS CIUDADANOS]: {DIAGNOSTICOS_CIUDADANOS}
[ESTRUCTURA DE ORATORIA CLÁSICA]: {ESTRUCTURAS_ORATORIA}

METODOLOGÍA ESTRICTA (Debes guiar al usuario paso a paso sin saltarte ninguno):

PASO 1: GENERACIÓN (Pensamiento Lateral)
- Escucha la idea del líder.
- Si la idea es aburrida o convencional (ej. "hacer un parque"), usa pensamiento lateral para darle un giro innovador cruzando conceptos. 
- Pregunta al usuario si aprueba el giro innovador.

PASO 2: VALIDACIÓN DEDUCTIVA (Lógica)
- Una vez la idea es innovadora, CRÚZALA obligatoriamente con los [DATOS ABIERTOS] y [DIAGNÓSTICOS CIUDADANOS].
- Pregunta al usuario: "¿Cómo cubriremos el presupuesto considerando que el límite es X?" o "¿Cómo esto responde a la petición ciudadana Y?".
- No pases al Paso 3 hasta que la idea sea 100% realizable y justificada con datos reales.

PASO 3: ORATORIA (Discurso de 2 minutos)
- Cuando el proyecto esté validado, redacta el discurso final utilizando exactamente la [ESTRUCTURA DE ORATORIA CLÁSICA].
- El discurso debe ser apasionado, directo y diseñado para ser defendido en la plaza pública o asamblea.
"""

# ==========================================
# 4. INTERFAZ Y LÓGICA DE ESTADO
# ==========================================
st.title("🏛️ SYLLATERAL AI")
st.markdown("*La información nace, crece, se reproduce pero no debe morir.*")

# Panel Lateral: Monitores de Datos Cívicos
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

# Inicialización segura del cliente y chat
if "chat_session" not in st.session_state or st.session_state.get("current_api_key") != api_key:
    try:
        client = genai.Client(api_key=api_key)
        st.session_state.chat_session = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=INSTRUCCION_SISTEMA,
                temperature=0.6,
            )
        )
        st.session_state.current_api_key = api_key
    except Exception as e:
        st.error(f"Error al conectar con la API Key ingresada: {e}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bienvenido al motor de **SYLLATERAL AI**. Para comenzar la Fase 1 (Generación), cuéntame: ¿Qué problemática de tu comunidad quieres resolver hoy?"}
    ]

# Renderizar historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Captura de input del usuario
if user_input := st.chat_input("Plantea tu idea, responde a la validación o pide el discurso..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Analizando con Pensamiento Lateral y Lógica Deductiva..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error al generar respuesta: {e}")
