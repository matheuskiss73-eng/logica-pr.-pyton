import streamlit as st
import time

st.title("laço de repetição - For")

st.header("CONTAGEM.")

if st.button("iniciar"):
    for i in range (100,122,2):
        st.write(i)
        time.sleep(1)
    st.header("FIM")