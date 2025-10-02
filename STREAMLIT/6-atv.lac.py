import streamlit as st
import time


st.title("MÉDIA")

n1 = st.number_input("digite primeira nota:", min_value=0)
n2 = st.number_input("digite segunda nota: ", min_value=0)
n3 = st.number_input("digite terceira nota: ", min_value=0)
n4 = st.number_input("digite quarta nota: ", min_value=0)


media = n1 + n2 + n3 + n4 /4



if  st.button("calcular sua media"):
      st.write(f"SUA MÉDIA É: {media}")