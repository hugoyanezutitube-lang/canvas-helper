import streamlit as st

# ====================== MODELO DE APRENDIZAJE AUTOMÁTICO ======================
def bot_canvas_respuesta(mensaje: str, nombre: str) -> str:
    mensaje = mensaje.lower().strip()
    
    reglas = {
        ("hola", "buenas", "saludos", "hey"): f"¡Hola {nombre}! 😊 ¿En qué te ayudo con Canvas LMS?",
        ("cómo estás", "qué tal"): f"¡Muy bien! ¿Y tú, {nombre}?",
        ("gracias", "muchas gracias"): f"¡De nada, {nombre}! Siempre aquí para ayudarte 🚀",
        ("adiós", "chau", "hasta luego"): f"¡Hasta pronto, {nombre}! Éxitos en tus cursos 😊",

        # Dudas más frecuentes
        ("editar perfil", "cambiar perfil", "foto de perfil", "perfil"):
            "Para editar tu perfil:\n1. Cuenta (menú izquierdo) → Perfil\n2. Clic en **Editar Perfil**\n3. Cambia nombre, biografía o foto.\n4. Guarda.",
        
        ("subir tarea", "entregar tarea", "cómo subir", "enviar assignment"):
            "Para subir una tarea:\n1. Entra al curso → **Tareas**\n2. Selecciona la tarea\n3. Clic en **Enviar tarea**\n4. Sube archivo o escribe texto\n5. Clic en **Enviar**.",
        
        ("contraseña", "olvidé contraseña", "resetear"):
            "Ve a la página de login → **¿Olvidaste tu contraseña?** → ingresa tu correo institucional.",
        
        ("calificaciones", "ver notas", "grades"):
            "En el menú izquierdo del curso → **Calificaciones**.",
        
        ("ayuda", "faq", "preguntas"):
            "Aquí tienes las dudas más comunes:\n• Subir tareas\n• Editar perfil\n• Ver calificaciones\n• Restablecer contraseña\n¿Qué necesitas exactamente?",
    }
    
    for palabras, respuesta in reglas.items():
        if any(p in mensaje for p in palabras):
            return respuesta
    
    return f"Entendido, {nombre}. ¿Me das más detalles? Puedo ayudarte con tareas, perfil, calificaciones, etc. 😊"

# ====================== INTERFAZ DE LA APP ======================
st.set_page_config(page_title="Canvas Helper", page_icon="🎓", layout="centered")

st.title("🎓 Canvas Helper")
st.markdown("**Tu asistente inteligente para Canvas LMS** – Pregúntame lo que quieras")

# Guardar nombre del estudiante
if "nombre" not in st.session_state:
    nombre = st.text_input("👤 ¿Cuál es tu nombre?", placeholder="Escribe tu nombre...")
    if st.button("Empezar"):
        if nombre.strip():
            st.session_state.nombre = nombre.strip().title()
            st.rerun()
        else:
            st.warning("Por favor ingresa tu nombre")
else:
    st.success(f"¡Hola {st.session_state.nombre}! 😊")

    # Chatbot
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

    # Mostrar historial
    for msg in st.session_state.mensajes:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input del usuario
    if prompt := st.chat_input("Escribe tu duda sobre Canvas..."):
        st.session_state.mensajes.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        respuesta = bot_canvas_respuesta(prompt, st.session_state.nombre)
        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.markdown(respuesta)

    # Sidebar con FAQs rápidas
    with st.sidebar:
        st.header("❓ Preguntas Frecuentes")
        faqs = [
            "Cómo subir una tarea",
            "Cómo editar mi perfil",
            "Cómo cambiar foto de perfil",
            "Cómo ver mis calificaciones",
            "Olvidé mi contraseña",
        ]
        for pregunta in faqs:
            if st.button(pregunta):
                st.session_state.mensajes.append({"role": "user", "content": pregunta})
                respuesta = bot_canvas_respuesta(pregunta.lower(), st.session_state.nombre)
                st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
                st.rerun()

        st.caption("Versión 1.0 - Creado con Streamlit + Modelo de coincidencias")

# ====================== INSTRUCCIONES PARA COMPARTIR ======================
if "nombre" not in st.session_state:
    st.info("👆 Ingresa tu nombre para activar el asistente")
else:
    st.info("¡Listo! Comparte esta app con tus estudiantes. Ellos podrán usarla directamente.")
