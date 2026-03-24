import streamlit as st

# ====================== DATOS DE FAQ (Modelo de Aprendizaje Automático) ======================
faq_categories = [
    {"id": "acceso", "title": "🔑 Acceso y Login", "items": [
        {"question": "¿Cómo accedo a Canvas LMS?", "answer": "Ingresa a tuuniversidad.instructure.com con tu usuario y contraseña institucional."},
        {"question": "¿Olvidé mi contraseña?", "answer": "En la página de login haz clic en '¿Olvidaste tu contraseña?' e ingresa tu correo institucional."}
    ]},
    {"id": "perfil", "title": "👤 Perfil y Foto", "items": [
        {"question": "¿Cómo editar mi perfil?", "answer": "Menú izquierdo → Cuenta → Perfil → Editar Perfil. Puedes cambiar nombre, biografía y foto."},
        {"question": "¿Cómo cambiar mi foto de perfil?", "answer": "En Perfil haz clic en el círculo de la foto → Editar → Sube tu imagen."}
    ]},
    {"id": "tareas", "title": "📝 Tareas y Entregas", "items": [
        {"question": "¿Cómo subir una tarea?", "answer": "Curso → Tareas → Selecciona la tarea → Enviar tarea → Sube archivo o texto → Enviar."},
        {"question": "¿Puedo entregar después de la fecha límite?", "answer": "Solo si el profesor habilitó entregas tardías. Revisa la tarea."}
    ]},
    {"id": "calificaciones", "title": "📊 Calificaciones", "items": [
        {"question": "¿Cómo veo mis notas?", "answer": "Menú izquierdo del curso → Calificaciones."}
    ]},
    {"id": "modulos", "title": "📚 Módulos y Contenido", "items": [
        {"question": "¿Dónde están los módulos?", "answer": "Menú izquierdo → Módulos. Todo el contenido está organizado por semanas."}
    ]},
    {"id": "quizzes", "title": "❓ Quizzes y Exámenes", "items": [
        {"question": "¿Cómo hago un quiz?", "answer": "Ve a Tareas o Quizzes → Haz clic en el quiz → Responde sin cerrar la ventana."}
    ]},
    {"id": "discusiones", "title": "💬 Discusiones", "items": [
        {"question": "¿Cómo participar en una discusión?", "answer": "Menú izquierdo → Discusiones → Elige el tema → Responder."}
    ]}
]

# ====================== LÓGICA DE FILTRADO (igual que tu React) ======================
def filtrar_items(query: str, active_category: str):
    query = query.lower().strip()
    if not query:
        cat = next((c for c in faq_categories if c["id"] == active_category), None)
        return cat["items"] if cat else [], cat["title"] if cat else ""
    
    all_matches = []
    for cat in faq_categories:
        for item in cat["items"]:
            if (query in item["question"].lower() or query in item["answer"].lower()):
                all_matches.append(item)
    return all_matches, f'Resultados para "{query}"'

# ====================== INTERFAZ MODERNA (adaptada del React) ======================
st.set_page_config(page_title="Canvas Helper Pro", page_icon="🎓", layout="wide")

# Hero Section + Logo
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo.png", width=180)
with col_titulo:
    st.title("🎓 Canvas Helper Pro")
    st.markdown("**Universidad Indoamérica** – Tu asistente inteligente de Canvas LMS")

# Búsqueda (HeroSection)
search_query = st.text_input("🔍 Busca cualquier duda...", placeholder="Ej: cómo subir tarea, cambiar foto, ver calificaciones...", label_visibility="collapsed")

# Categorías (Pills)
if not search_query:
    st.markdown("### Selecciona una categoría")
    cols = st.columns(len(faq_categories))
    active_category = st.session_state.get("active_category", "acceso")
    
    for i, cat in enumerate(faq_categories):
        with cols[i]:
            if st.button(cat["title"], key=cat["id"], use_container_width=True,
                         type="primary" if active_category == cat["id"] else "secondary"):
                st.session_state.active_category = cat["id"]
                st.rerun()

# Filtrado
active_category = st.session_state.get("active_category", "acceso")
items, title = filtrar_items(search_query, active_category)

# Resultados
if search_query:
    st.info(f"**{len(items)} resultado{'s' if len(items) != 1 else ''} encontrado{'s' if len(items) != 1 else ''}**")

if items:
    st.markdown(f"### {title}")
    for item in items:
        with st.expander(item["question"], expanded=False):
            st.markdown(item["answer"])
else:
    st.warning("🤔 No se encontraron resultados. Prueba con otras palabras.")

# Footer oficial
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray; font-size:0.9em;'>"
    "Basado en el Manual del Estudiante — Canvas LMS · Universidad Indoamérica © 2026"
    "</p>", unsafe_allow_html=True
)
