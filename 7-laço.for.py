import streamlit as st
import time

st.title("laço de repetição - For")

st.header("CONTAGEM.")

numero = st.number_input("informe um numero", step=1)

if st.button("iniciar"):
    for i in range (1,numero+1):
        st.write(i)
        time.sleep(1)
    st.header("FIM")