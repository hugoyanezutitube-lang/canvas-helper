import streamlit as st

# ====================== CONFIG ======================
st.set_page_config(
    page_title="Canvas Helper Pro",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================== ESTILOS ======================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #ffffff 35%, #f8fafc 100%);
    }

    .main-container {
        max-width: 980px;
        margin: 0 auto;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #334155 100%);
        padding: 2.2rem 2rem;
        border-radius: 24px;
        color: white;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.18);
        margin-bottom: 1.8rem;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.16);
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 0.6rem;
    }

    .hero-subtitle {
        color: rgba(255,255,255,0.84);
        font-size: 1rem;
        line-height: 1.6;
        max-width: 720px;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0f172a;
        margin-top: 0.4rem;
        margin-bottom: 0.9rem;
    }

    .results-count {
        font-size: 0.95rem;
        color: #64748b;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }

    .category-chip {
        text-align: center;
        font-size: 0.95rem;
        padding: 0.8rem 1rem;
        border-radius: 16px;
        font-weight: 600;
        background: white;
        border: 1px solid #e2e8f0;
        color: #0f172a;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
    }

    .empty-state {
        text-align: center;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 22px;
        padding: 3rem 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    .empty-emoji {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .empty-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.25rem;
    }

    .empty-subtitle {
        color: #64748b;
        font-size: 0.95rem;
    }

    .footer-box {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        padding: 1rem 0 0.5rem 0;
    }

    div[data-testid="stExpander"] {
        border: 1px solid #e2e8f0 !important;
        border-radius: 18px !important;
        background: white !important;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
        margin-bottom: 0.85rem;
        overflow: hidden;
    }

    div[data-testid="stExpander"] summary {
        font-weight: 700;
        color: #0f172a;
        padding-top: 0.2rem;
        padding-bottom: 0.2rem;
    }

    .faq-category-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0f172a;
        margin-top: 0.25rem;
        margin-bottom: 1rem;
    }

    .logo-wrap {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .helper-note {
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }

    hr {
        margin-top: 2rem !important;
        margin-bottom: 0.75rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ====================== DATOS FAQ ======================
faq_categories = [
    {
        "id": "acceso",
        "title": "🔑 Acceso y Login",
        "items": [
            {
                "question": "¿Cómo accedo a Canvas LMS?",
                "answer": "Ingresa a tuuniversidad.instructure.com con tu usuario y contraseña institucional."
            },
            {
                "question": "¿Olvidé mi contraseña?",
                "answer": "En la página de inicio de sesión, haz clic en '¿Olvidaste tu contraseña?' e ingresa tu correo institucional."
            }
        ]
    },
    {
        "id": "perfil",
        "title": "👤 Perfil y Foto",
        "items": [
            {
                "question": "¿Cómo editar mi perfil?",
                "answer": "Ve al menú izquierdo → Cuenta → Perfil → Editar perfil. Allí puedes cambiar tu nombre, biografía y foto."
            },
            {
                "question": "¿Cómo cambiar mi foto de perfil?",
                "answer": "En tu perfil, haz clic sobre la imagen actual → Editar → Sube tu nueva fotografía."
            }
        ]
    },
    {
        "id": "tareas",
        "title": "📝 Tareas y Entregas",
        "items": [
            {
                "question": "¿Cómo subir una tarea?",
                "answer": "Ingresa al curso → Tareas → Selecciona la actividad → Entregar tarea → Sube el archivo o escribe el texto → Enviar."
            },
            {
                "question": "¿Puedo entregar después de la fecha límite?",
                "answer": "Solo si el docente habilitó entregas tardías. Revisa la configuración de la tarea."
            }
        ]
    },
    {
        "id": "calificaciones",
        "title": "📊 Calificaciones",
        "items": [
            {
                "question": "¿Cómo veo mis notas?",
                "answer": "Dentro del curso, ve al menú izquierdo y haz clic en Calificaciones."
            }
        ]
    },
    {
        "id": "modulos",
        "title": "📚 Módulos y Contenido",
        "items": [
            {
                "question": "¿Dónde están los módulos?",
                "answer": "En el menú izquierdo selecciona Módulos. Allí encontrarás el contenido organizado por semanas o unidades."
            }
        ]
    },
    {
        "id": "quizzes",
        "title": "❓ Quizzes y Exámenes",
        "items": [
            {
                "question": "¿Cómo hago un quiz?",
                "answer": "Ve a Tareas o Quizzes → selecciona el cuestionario → responde cada pregunta y envía antes de cerrar."
            }
        ]
    },
    {
        "id": "discusiones",
        "title": "💬 Discusiones",
        "items": [
            {
                "question": "¿Cómo participar en una discusión?",
                "answer": "Dentro del curso, entra a Discusiones → abre el tema → haz clic en Responder."
            }
        ]
    }
]

# ====================== ESTADO ======================
if "active_category" not in st.session_state:
    st.session_state.active_category = "acceso"

# ====================== FUNCIONES ======================
def filtrar_items(query: str, active_category: str):
    query = query.lower().strip()

    if not query:
        cat = next((c for c in faq_categories if c["id"] == active_category), None)
        return {
            "items": cat["items"] if cat else [],
            "title": cat["title"] if cat else ""
        }

    all_matches = []
    for cat in faq_categories:
        for item in cat["items"]:
            if query in item["question"].lower() or query in item["answer"].lower():
                all_matches.append(item)

    return {
        "items": all_matches,
        "title": f'Resultados para "{query}"'
    }

# ====================== LAYOUT ======================
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# HERO
col1, col2 = st.columns([1, 4], vertical_alignment="center")
with col1:
    try:
        st.image("logo.png", width=120)
    except:
        st.markdown("## 🎓")

with col2:
    st.markdown("""
        <div class="hero-box">
            <div class="hero-badge">Universidad Indoamérica</div>
            <div class="hero-title">Canvas Helper Pro</div>
            <div class="hero-subtitle">
                Tu asistente de ayuda para resolver dudas frecuentes sobre el uso de Canvas LMS:
                acceso, tareas, calificaciones, módulos, quizzes y más.
            </div>
        </div>
    """, unsafe_allow_html=True)

# BÚSQUEDA
search_query = st.text_input(
    "Buscar",
    placeholder="Ej: cómo subir tarea, cambiar foto, ver calificaciones...",
    label_visibility="collapsed"
)

# CATEGORÍAS
if not search_query:
    st.markdown('<div class="section-title">Selecciona una categoría</div>', unsafe_allow_html=True)

    cols = st.columns(len(faq_categories))
    for i, cat in enumerate(faq_categories):
        with cols[i]:
            is_active = st.session_state.active_category == cat["id"]
            if st.button(
                cat["title"],
                key=f"cat_{cat['id']}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.active_category = cat["id"]
                st.rerun()

# FILTRO
filtered = filtrar_items(search_query, st.session_state.active_category)
items = filtered["items"]
title = filtered["title"]

# CONTADOR DE RESULTADOS
if search_query:
    total = len(items)
    st.markdown(
        f'<div class="results-count">{total} resultado{"s" if total != 1 else ""} encontrado{"s" if total != 1 else ""}</div>',
        unsafe_allow_html=True
    )

# RESULTADOS
if items:
    st.markdown(f'<div class="faq-category-title">{title}</div>', unsafe_allow_html=True)

    for item in items:
        with st.expander(item["question"], expanded=False):
            st.write(item["answer"])
else:
    st.markdown("""
        <div class="empty-state">
            <div class="empty-emoji">🤔</div>
            <div class="empty-title">No se encontraron resultados</div>
            <div class="empty-subtitle">Intenta con otros términos de búsqueda</div>
        </div>
    """, unsafe_allow_html=True)

# FOOTER
st.divider()
st.markdown("""
    <div class="footer-box">
        Basado en el Manual del Estudiante — Canvas LMS · Universidad Indoamérica © 2026
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
