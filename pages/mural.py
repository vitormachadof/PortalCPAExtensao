import html
import logging
from datetime import date, datetime
from typing import Any

import streamlit as st

from services.devolutivas import get_public_devolutivas

LOGGER = logging.getLogger(__name__)


def _text(value: Any) -> str:
    return str(value or "").strip()


def _publication_date(value: Any) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).date()
    except ValueError:
        return None


def _format_date(value: Any) -> str:
    publication_date = _publication_date(value)
    if publication_date is None:
        return "Data não informada"
    return publication_date.strftime("%d/%m/%Y")


def _matches_search(devolutiva: dict[str, Any], search: str) -> bool:
    if not search:
        return True
    searchable_text = " ".join(
        _text(devolutiva.get(field))
        for field in ("titulo", "demanda", "resposta")
    )
    return search.casefold() in searchable_text.casefold()


def _filter_devolutivas(
    devolutivas: list[dict[str, Any]],
    area: str,
    year: str,
    search: str,
) -> list[dict[str, Any]]:
    filtered: list[dict[str, Any]] = []
    for devolutiva in devolutivas:
        publication_date = _publication_date(devolutiva.get("data_publicacao"))
        matches_area = (
            area == "Todas as áreas"
            or _text(devolutiva.get("area")) == area
        )
        matches_year = (
            year == "Todos os anos"
            or (
                publication_date is not None
                and str(publication_date.year) == year
            )
        )
        if matches_area and matches_year and _matches_search(devolutiva, search):
            filtered.append(devolutiva)
    return filtered


def _render_devolutiva(devolutiva: dict[str, Any]) -> None:
    area = html.escape(_text(devolutiva.get("area")) or "Área não informada")
    title = html.escape(_text(devolutiva.get("titulo")) or "Devolutiva")
    demand = html.escape(_text(devolutiva.get("demanda")) or "Não informada.")
    response = html.escape(_text(devolutiva.get("resposta")) or "Não informada.")
    publication_date = html.escape(
        f"Publicado em {_format_date(devolutiva.get('data_publicacao'))}"
    )

    with st.container(border=True):
        st.markdown(
            f"""
            <div class="devolutiva-header">
                <strong>{area}</strong>
                <span>{publication_date}</span>
            </div>
            <h3 class="devolutiva-title">{title}</h3>
            <div class="devolutiva-label">DEMANDA DA PESQUISA</div>
            <div class="devolutiva-text">{demand}</div>
            <div class="devolutiva-label">RESPOSTA DA ÁREA</div>
            <div class="devolutiva-text">{response}</div>
            """,
            unsafe_allow_html=True,
        )


st.title("MURAL DE DEVOLUTIVAS")
st.write("Respostas das áreas às demandas levantadas nas pesquisas da CPA.")

try:
    devolutivas = get_public_devolutivas()
except Exception:
    LOGGER.exception("Falha ao consultar as devolutivas públicas.")
    st.error(
        "Não foi possível carregar as devolutivas agora. "
        "Tente novamente mais tarde."
    )
    st.stop()

areas = sorted(
    {
        _text(devolutiva.get("area"))
        for devolutiva in devolutivas
        if _text(devolutiva.get("area"))
    },
    key=str.casefold,
)
years = sorted(
    {
        _publication_date(devolutiva.get("data_publicacao")).year
        for devolutiva in devolutivas
        if _publication_date(devolutiva.get("data_publicacao")) is not None
    },
    reverse=True,
)

area_column, year_column, search_column = st.columns(3)
with area_column:
    selected_area = st.selectbox(
        "Área",
        ["Todas as áreas", *areas],
        key="mural_area",
    )
with year_column:
    selected_year = st.selectbox(
        "Período",
        ["Todos os anos", *(str(year) for year in years)],
        key="mural_year",
    )
with search_column:
    search = st.text_input(
        "Buscar",
        placeholder="Palavra-chave",
        key="mural_search",
    ).strip()

filtered_devolutivas = _filter_devolutivas(
    devolutivas,
    selected_area,
    selected_year,
    search,
)

if not filtered_devolutivas:
    st.info("Nenhuma devolutiva encontrada.")
else:
    for devolutiva in filtered_devolutivas:
        _render_devolutiva(devolutiva)
