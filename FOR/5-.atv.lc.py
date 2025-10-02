import streamlit as st
import time

st.title("ímpares e pares")

par = 0
imp = 0


for i in range (1,6):

    numero = print(f"Digite o {i}º número: ")
    if numero % 2 == 0:
        par = par + 1
    else:
        imp = imp + 1


print(f"Quantidades de numeros ímpares: {imp}")
print(f"Quantidades de numeros pares: {par}")


