import streamlit as st

from functions.rechnungen import add, subtract, square, root

st.title("")
st.write(" ")

with st.form("Addieren"):
    st.write("Gib hier deine Zahlen die du addieren willst ein:")
    a = st.number_input("Nummer 1")
    b = st.number_input("Nummer 2")
    submitted = st.form_submit_button("Berechnen")