import html
from collections.abc import Mapping
from typing import Any

import streamlit as st


UNAVAILABLE_MESSAGE = "Informação indisponível no momento"


def _text(value: Any) -> str:
    return str(value).strip() if value is not None else ""


def _contact_config() -> dict[str, str]:
    section = st.secrets.get("contato", {})
    if not isinstance(section, Mapping):
        return {}
    return {
        key: _text(section.get(key))
        for key in ("chat_url", "meet_url", "email", "horario")
    }


def _render_link_or_fallback(label: str, url: str) -> None:
    if url:
        st.link_button(label, url, use_container_width=False)
    else:
        st.markdown(
            f'<p class="contact-unavailable">{UNAVAILABLE_MESSAGE}</p>',
            unsafe_allow_html=True,
        )


def _render_contact_card(
    *,
    key: str,
    title: str,
    description: str,
    button_label: str,
    url: str,
) -> None:
    with st.container(key=key):
        st.markdown(
            f"""
            <div class="contact-card-content">
                <h2>{html.escape(title)}</h2>
                <p>{html.escape(description)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        _render_link_or_fallback(button_label, url)


def _render_info_value(value: str, *, email: bool = False) -> str:
    if not value:
        return f'<span class="contact-unavailable">{UNAVAILABLE_MESSAGE}</span>'
    escaped_value = html.escape(value)
    if email:
        return f'<a href="mailto:{escaped_value}">{escaped_value}</a>'
    return escaped_value


config = _contact_config()

st.title("FALE COM A CPA")
st.write(
    "Tire dúvidas, envie sugestões ou marque uma conversa com a coordenação "
    "da CPA."
)

chat_column, meet_column = st.columns(2)
with chat_column:
    _render_contact_card(
        key="contact-chat-card",
        title="GOOGLE CHAT",
        description="Mensagem rápida para a equipe da CPA.",
        button_label="Abrir o Chat",
        url=config["chat_url"],
    )
with meet_column:
    _render_contact_card(
        key="contact-meet-card",
        title="GOOGLE MEET",
        description="Reunião por vídeo com a coordenação da CPA.",
        button_label="Entrar na sala",
        url=config["meet_url"],
    )

st.markdown(
    f"""
    <div class="contact-info-strip">
        <div>
            <strong>ATENDIMENTO</strong>
            <span>{_render_info_value(config["horario"])}</span>
        </div>
        <div>
            <strong>E-MAIL</strong>
            <span>{_render_info_value(config["email"], email=True)}</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
