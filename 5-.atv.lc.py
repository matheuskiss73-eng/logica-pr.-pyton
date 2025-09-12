import streamlit as st
import time

st.title("ímpares e pares")

par = 0
imp = 0


for i in range (1,6):

    numero = st.number_input(f"Digite o {i}º número: ", step=1)
    if numero % 2 == 0:
        par = par + 1
    else:
        imp = imp + 1

if  st.button("Verificar"):
    st.info(f"Quantidades de numeros ímpares: {imp}")
    st.info(f"Quantidades de numeros pares: {par}")