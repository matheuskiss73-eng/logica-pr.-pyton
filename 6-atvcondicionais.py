import streamlit as st

st.title("CALCULADORA")

n1 = st.number_input("digite primeiro numero: ")
n2 = st.number_input("digite segundo numero: ")

soma = n1 + n2
media = n1 + n2 /2
produto = n1 * n2
maxi = max(n1,n2)
mini = min(n1,n2)

if  st.button("calcular"):
     st.write(f"soma: {soma}")
     st.write(f"media: {media}")
     st.write(f"produto: {produto}")
     st.write(f"maxi: {maxi}")
     st.write(f"mini: {mini}")
else:
     st.info("INFORME OS VALORES")