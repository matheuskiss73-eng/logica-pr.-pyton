import streamlit as st
import time

st.title("COMTAGEM ÍMPAR")

st.header("CONTAGEM.")

if st.button("iniciar"):
    for i in range (1,21,2):
        st.write(i)
        time.sleep(2)
    st.header("FIM")