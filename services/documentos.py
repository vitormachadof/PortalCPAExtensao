from typing import Any

import streamlit as st

from services.db import get_supabase_client

DOCUMENTOS_COLUMNS = "id, titulo, tipo, ano, caminho_arquivo, publico"
DOCUMENTOS_BUCKET = "documentos"
SIGNED_URL_SECONDS = 600


@st.cache_data(ttl=300)
def get_documentos(authorized: bool) -> list[dict[str, Any]]:
    """Busca documentos conforme a permissão efetiva do usuário."""
    query = (
        get_supabase_client()
        .table("documentos")
        .select(DOCUMENTOS_COLUMNS)
    )
    if not authorized:
        query = query.eq("publico", True)

    response = query.order("ano", desc=True).order("titulo").execute()
    return list(response.data or [])


def create_document_signed_url(file_path: str) -> str:
    """Gera um link temporário para um arquivo do bucket privado."""
    response = (
        get_supabase_client()
        .storage.from_(DOCUMENTOS_BUCKET)
        .create_signed_url(file_path, SIGNED_URL_SECONDS)
    )
    if isinstance(response, dict):
        signed_url = response.get("signedURL") or response.get("signedUrl")
    else:
        signed_url = getattr(response, "signedURL", None) or getattr(
            response, "signedUrl", None
        )
    if not signed_url:
        raise RuntimeError("O Storage não retornou um link temporário.")
    return str(signed_url)
