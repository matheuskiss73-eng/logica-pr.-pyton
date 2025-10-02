import streamlit as st
import time

st.title("TABUADA")

st.header("TABUADA DE 5.")

numero = st.number_input("informe um numero", step = 1)

if st.button("Iniciar tabuada"):

     for i in range (1,11):
        time.sleep(1)
        n = numero * i
     
        st.info(f"{numero} x {i} = {n}")

st.header("FIM")