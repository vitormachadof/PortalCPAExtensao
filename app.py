from pathlib import Path

import streamlit as st

from services.auth import UserState, get_current_user


st.set_page_config(
    page_title="Portal CPA",
    layout="wide",
)


def load_css() -> None:
    css_path = Path(__file__).resolve().parent / "assets" / "style.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


load_css()

current_user = get_current_user()

st.markdown(
    """
    <div class="topbar">
        <div class="topbar-inner">
            <div class="portal-brand">PORTAL CPA</div>
            <div class="portal-subtitle">Comissão Própria de Avaliação</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

def render_user_access(user: UserState) -> None:
    if user.access_denied:
        st.error("Acesso não autorizado")

    if user.authorized:
        with st.container():
            identity_column, action_column = st.columns([5, 1])
            with identity_column:
                st.markdown(
                    f"**Olá, {user.name} · Perfil: {user.profile}**"
                )
            with action_column:
                if st.button("Sair", use_container_width=True):
                    st.logout()
                    st.rerun()
    else:
        if st.button("Entrar com conta Impacta"):
            st.login()


render_user_access(current_user)

public_pages = [
    st.Page("pages/mural.py", title="Mural de devolutivas"),
    st.Page("pages/relatorios.py", title="Relatórios e boletins"),
    st.Page("pages/contato.py", title="Contato"),
]

if current_user.authorized:
    pages = {
        "ACESSO RÁPIDO": [
            st.Page("pages/inicio.py", title="Início", default=True),
            st.Page("pages/dashboards.py", title="Dashboards"),
            *public_pages,
        ]
    }
else:
    pages = {
        "ACESSO RÁPIDO": [
            st.Page("pages/mural.py", title="Mural de devolutivas", default=True),
            *public_pages[1:],
        ]
    }

navigation = st.navigation(pages)
navigation.run()
