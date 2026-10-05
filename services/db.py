import streamlit as st
from supabase import Client, create_client


@st.cache_resource
def get_supabase_client() -> Client:
    """Cria o cliente Supabase usando somente os secrets da aplicação."""
    try:
        supabase_secrets = st.secrets["supabase"]
        url = str(supabase_secrets["url"])
        key = str(supabase_secrets["key"])
    except (KeyError, TypeError) as error:
        raise RuntimeError(
            "Configure supabase.url e supabase.key em st.secrets."
        ) from error

    if not url or not key:
        raise RuntimeError("Configure supabase.url e supabase.key em st.secrets.")

    return create_client(url, key)
