import streamlit as st

# ====================== MODELO DE APRENDIZAJE AUTOMÁTICO V2.1 (con logo) ======================
def bot_canvas_respuesta(mensaje: str, nombre: str) -> str:
    mensaje = mensaje.lower().strip()
    
    reglas = {
        ("hola", "buenas", "saludos", "hey"): f"¡Hola {nombre}! 😊 ¿En qué te ayudo hoy con Canvas LMS?",
        ("cómo estás", "qué tal"): f"¡Muy bien! ¿Y tú, {nombre}?",
        ("gracias", "muchas gracias"): f"¡De nada, {nombre}! 🚀",
        ("adiós", "chau", "hasta luego"): f"¡Hasta pronto, {nombre}! Éxitos en tus cursos 😊",

        # Todas las reglas anteriores (perfil, tareas, calificaciones, etc.)
        ("editar perfil", "cambiar perfil", "foto de perfil", "perfil"): 
            "Para editar tu perfil:\n1. Menú izquierdo → **Cuenta** → **Perfil**\n2. Clic en **Editar Perfil**\n3. Cambia nombre, biografía o foto.\n4. Guarda.",
        
        ("subir tarea", "entregar tarea", "enviar assignment", "cómo subir"): 
            "Para subir una tarea:\n1. Entra al curso → **Tareas**\n2. Selecciona la tarea\n3. Clic en **Enviar tarea**\n4. Sube archivo o escribe\n5. Clic en **Enviar**.",
        
        ("calificaciones", "ver notas", "grades", "notas"): 
            "Ve al menú izquierdo del curso → **Calificaciones**.",
        
        ("contraseña", "olvidé contraseña", "resetear"): 
            "En la página de login → **¿Olvidaste tu contraseña?** → ingresa tu correo institucional.",
        
        ("módulos", "ver módulos"): 
            "Menú izquierdo → **Módulos**.",
        
        ("quiz", "examen", "prueba"): 
            "Ve a **Tareas** o **Quizzes** → haz clic en el quiz.",
        
        ("ayuda", "faq", "preguntas"): 
            "¡Estoy aquí para todo! Usa los botones o escribe tu duda.",
    }
    
    for palabras, respuesta in reglas.items():
        if any(p in mensaje for p in palabras):
            return respuesta
    
    return f"Entendido, {nombre}. ¿Me das más detalles? 😊"

# ====================== INTERFAZ CON LOGO ======================
st.set_page_config(page_title="Canvas Helper Pro", page_icon="🎓", layout="wide")

# Mostrar logo de tu universidad (se carga automáticamente del GitHub)
st.image("logo.png", width=280)   # ← Aquí aparece tu logo

st.title("🎓 Canvas Helper Pro")
st.markdown("**Tu asistente inteligente de Canvas LMS** – Versión 2.1")

# El resto del código es igual que antes (nombre, chat, preguntas rápidas, sidebar, etc.)
if "nombre" not in st.session_state:
    col1, col2 = st.columns([3,1])
    with col1:
        nombre = st.text_input("👤 ¿Cuál es tu nombre?", placeholder="Escribe tu nombre completo...")
    with col2:
        if st.button("🚀 Empezar", type="primary"):
            if nombre.strip():
                st.session_state.nombre = nombre.strip().title()
                st.rerun()
            else:
                st.warning("Por favor ingresa tu nombre")
else:
    st.success(f"¡Bienvenido/a {st.session_state.nombre}! 😊")

    tab1, tab2 = st.tabs(["💬 Chat Inteligente", "❓ Preguntas Rápidas"])

    with tab1:
        if "mensajes" not in st.session_state:
            st.session_state.mensajes = []
        for msg in st.session_state.mensajes:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        if prompt := st.chat_input("Escribe tu duda sobre Canvas..."):
            st.session_state.mensajes.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            respuesta = bot_canvas_respuesta(prompt, st.session_state.nombre)
            st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
            with st.chat_message("assistant"):
                st.markdown(respuesta)

    with tab2:
        st.markdown("**Haz clic en cualquier botón** para respuesta instantánea:")
        cols = st.columns(3)
        preguntas = [
            "Cómo subir una tarea", "Cómo editar mi perfil", "Cómo ver mis calificaciones",
            "Olvidé mi contraseña", "Cómo ver los módulos", "Cómo hacer un quiz",
            "Cómo participar en una discusión", "Cómo subir archivos", "Ver calendario"
        ]
        for i, preg in enumerate(preguntas):
            with cols[i % 3]:
                if st.button(preg, use_container_width=True):
                    st.session_state.mensajes.append({"role": "user", "content": preg})
                    respuesta = bot_canvas_respuesta(preg.lower(), st.session_state.nombre)
                    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
                    st.rerun()

with st.sidebar:
    st.image("logo.png", width=150)   # Logo también en sidebar
    st.header("📚 Canvas Helper Pro")
    st.caption("Versión 2.1 - Con logo de tu universidad")

st.caption("💡 Sube logo.png y Streamlit lo muestra automáticamente")
