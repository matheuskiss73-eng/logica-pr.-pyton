import streamlit as st

st.title("laço de repetição - For")
st.subheader("LOGIN")


usuario1 = "matheus"
senha1 = "123456"

usuario = st.text_input("digite o nome do usuario: ")
senha = st.text_input("digite sua senha: ",type="password")
if st.button("ENTRAR"):
    if usuario1 == usuario and senha1 == senha:
        st.success(f"Bem vindo de volta!")
    else:
        st.warning("login ou senha invalidos")  
