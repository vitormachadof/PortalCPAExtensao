import streamlit as st

from services.auth import require_authenticated


require_authenticated()

st.title("DASHBOARDS")
st.write("Aba de dashboards em planejamento.")
