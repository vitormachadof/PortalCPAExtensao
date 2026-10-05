import streamlit as st

from services.auth import require_authenticated


require_authenticated()

st.title("INÍCIO")
st.write("Página inicial em desenvolvimento.")
