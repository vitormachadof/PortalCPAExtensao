from typing import Any

import streamlit as st

from services.db import get_supabase_client

DEVOLUTIVAS_COLUMNS = (
    "id, titulo, area, demanda, resposta, data_publicacao"
)


@st.cache_data(ttl=300)
def get_public_devolutivas() -> list[dict[str, Any]]:
    """Busca as devolutivas publicadas para o mural público."""
    response = (
        get_supabase_client()
        .table("devolutivas")
        .select(DEVOLUTIVAS_COLUMNS)
        .eq("publicado", True)
        .order("data_publicacao", desc=True)
        .execute()
    )
    return list(response.data or [])
