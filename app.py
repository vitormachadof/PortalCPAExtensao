from pathlib import Path

import streamlit as st


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

pages = {
    "ACESSO RÁPIDO": [
        st.Page("pages/inicio.py", title="Início", default=True),
        st.Page("pages/dashboards.py", title="Dashboards"),
        st.Page("pages/mural.py", title="Mural de devolutivas"),
        st.Page("pages/relatorios.py", title="Relatórios e boletins"),
        st.Page("pages/contato.py", title="Contato"),
    ]
}

navigation = st.navigation(pages)
navigation.run()
