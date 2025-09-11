import streamlit as st
import time

st.title("SOMAS")

n1 = st.number_input("digite primeiro numero:", step=1)
n2 = st.number_input("digite segundo numero: ", step=1)
n3 = st.number_input("digite terceiro numero: ", step=1)
n4 = st.number_input("digite quarto numero: ", step=1)
n5 = st.number_input("digite quinto numero: ", step=1)




for i in range (1):

 soma = n1 +  n2 + n3 + n4 + n5


if  st.button("calcular"):
     st.write(f"RESULTADO: {soma}")




    