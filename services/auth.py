from dataclasses import dataclass
from typing import Any

import streamlit as st

from services.db import get_supabase_client

AUTHORIZED_PROFILES = frozenset({"aluno", "coordenador", "avaliador", "admin"})
STUDENT_EMAIL_SUFFIX = "@aluno.impacta.edu.br"


@dataclass(frozen=True)
class UserState:
    """Representa o estado de autenticação usado pelo shell e pelas páginas."""

    authenticated: bool
    authorized: bool
    email: str | None = None
    name: str = "Visitante"
    profile: str = "visitante"
    access_denied: bool = False


def _user_value(user: Any, key: str, default: Any = None) -> Any:
    if isinstance(user, dict):
        return user.get(key, default)
    return getattr(user, key, default)


def _is_logged_in(user: Any) -> bool:
    return bool(_user_value(user, "is_logged_in", False))


def _provider_name(user: Any) -> str:
    name = _user_value(user, "name")
    if name:
        return str(name)
    return "Usuário Impacta"


def _resolve_database_user(email: str) -> dict[str, Any] | None:
    response = (
        get_supabase_client()
        .table("usuarios")
        .select("email, nome, perfil, ativo")
        .eq("email", email)
        .limit(1)
        .execute()
    )
    rows = response.data or []
    return rows[0] if rows else None


def get_current_user() -> UserState:
    """Resolve o usuário autenticado sem criar ou alterar registros."""
    user = st.user
    if not _is_logged_in(user):
        return UserState(authenticated=False, authorized=False)

    email_value = _user_value(user, "email")
    email = str(email_value).strip().lower() if email_value else ""
    if not email:
        return UserState(
            authenticated=True,
            authorized=False,
            name=_provider_name(user),
            access_denied=True,
        )

    database_user = _resolve_database_user(email)
    if database_user is not None:
        if not bool(database_user.get("ativo")):
            return UserState(
                authenticated=True,
                authorized=False,
                email=email,
                name=str(database_user.get("nome") or _provider_name(user)),
                access_denied=True,
            )

        profile = str(database_user.get("perfil") or "").strip().lower()
        if profile in AUTHORIZED_PROFILES:
            return UserState(
                authenticated=True,
                authorized=True,
                email=email,
                name=str(database_user.get("nome") or _provider_name(user)),
                profile=profile,
            )

        return UserState(
            authenticated=True,
            authorized=False,
            email=email,
            name=str(database_user.get("nome") or _provider_name(user)),
            access_denied=True,
        )

    if email.endswith(STUDENT_EMAIL_SUFFIX):
        return UserState(
            authenticated=True,
            authorized=True,
            email=email,
            name=_provider_name(user),
            profile="aluno",
        )

    return UserState(
        authenticated=True,
        authorized=False,
        email=email,
        name=_provider_name(user),
        access_denied=True,
    )


def require_authenticated(user: UserState | None = None) -> UserState:
    """Bloqueia uma página restrita quando não há perfil autorizado."""
    current_user = user or get_current_user()
    if not current_user.authorized:
        st.error("Acesso não autorizado")
        st.stop()
    return current_user
