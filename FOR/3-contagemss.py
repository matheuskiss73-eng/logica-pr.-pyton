import streamlit as st
import time

st.title("COMTAGEM 4")

st.header("CONTAGEM.")

numero = st.number_input("informe um numero", step=1)

if st.button("iniciar"):
    for i in range (numero,0,-1):
        st.write(i)
        time.sleep(1)
    st.header("FIM")