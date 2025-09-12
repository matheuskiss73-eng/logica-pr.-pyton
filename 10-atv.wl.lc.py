import streamlit as st

st.title("Laça de repetição - while")


nota = st.number_input("Digite um nota: ", step=1)

if st.button("Verificar"):
    if nota < 0 or nota > 10:
        st.warning("A nota de ser de 0 a 10")

    else:
        st.info(f"Nota: {nota}")