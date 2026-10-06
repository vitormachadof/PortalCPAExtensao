import html
import logging
from typing import Any

import streamlit as st

from services.auth import get_current_user
from services.documentos import create_document_signed_url, get_documentos

LOGGER = logging.getLogger(__name__)

TYPE_LABELS = {
    "relatorio": "Relatório",
    "boletim": "Boletim",
}


def _text(value: Any) -> str:
    return str(value or "").strip()


def _document_type(value: Any) -> str:
    return TYPE_LABELS.get(_text(value).lower(), "Documento")


def _filter_documents(
    documents: list[dict[str, Any]],
    selected_type: str,
    selected_year: str,
) -> list[dict[str, Any]]:
    filtered = documents
    if selected_type != "Todos":
        filtered = [
            document
            for document in filtered
            if _document_type(document.get("tipo")) == selected_type
        ]
    if selected_year != "Todos os anos":
        filtered = [
            document
            for document in filtered
            if str(document.get("ano") or "") == selected_year
        ]
    return filtered


def _render_document(document: dict[str, Any]) -> None:
    title = html.escape(_text(document.get("titulo")) or "Documento")
    document_type = html.escape(_document_type(document.get("tipo")))
    year = html.escape(_text(document.get("ano")) or "Ano não informado")
    is_restricted = not bool(document.get("publico"))

    with st.container(border=True):
        metadata_column, action_column = st.columns([5, 1])
        with metadata_column:
            st.markdown(
                f"""
                <div class="document-title">{title}</div>
                <div class="document-metadata">
                    <span>{document_type}</span>
                    <span>{year}</span>
                    {"<span class='document-restricted'>Restrito</span>" if is_restricted else ""}
                </div>
                """,
                unsafe_allow_html=True,
            )
        with action_column:
            try:
                signed_url = create_document_signed_url(
                    _text(document.get("caminho_arquivo"))
                )
            except Exception:
                LOGGER.exception("Falha ao gerar URL do documento.")
                st.warning("O download está temporariamente indisponível.")
            else:
                st.link_button(
                    "Baixar PDF",
                    signed_url,
                    use_container_width=True,
                )


st.title("RELATÓRIOS E BOLETINS")
st.write("Relatórios de autoavaliação e boletins informativos da CPA, em PDF.")

current_user = get_current_user()
try:
    documents = get_documentos(current_user.authorized)
except Exception:
    LOGGER.exception("Falha ao consultar os documentos.")
    st.error(
        "Não foi possível carregar os documentos agora. "
        "Tente novamente mais tarde."
    )
    st.stop()

available_years = sorted(
    {
        str(document.get("ano"))
        for document in documents
        if document.get("ano") is not None
    },
    reverse=True,
)

type_column, year_column = st.columns(2)
with type_column:
    selected_type = st.selectbox(
        "Tipo",
        ["Todos", "Relatório", "Boletim"],
        key="document_type",
    )
with year_column:
    selected_year = st.selectbox(
        "Ano",
        ["Todos os anos", *available_years],
        key="document_year",
    )

filtered_documents = _filter_documents(
    documents,
    selected_type,
    selected_year,
)

if not filtered_documents:
    st.info("Nenhum documento encontrado.")
else:
    for document in filtered_documents:
        _render_document(document)
