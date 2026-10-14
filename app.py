import streamlit as st

st.title("Hola Mundo, IA 👋")
nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"¡Hola Mundo, {nombre}! Esta es mi primera app en internet.")
