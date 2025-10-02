import streamlit as st

st.title("laço de repetição - For")
st.subheader("LOGIN")

usuario1 = "matheus"
senha1 = "123456"


st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("DIGITE SEU LOGIN:", disabled=st.session_state.desabilitar)
senha = st.text_input("DIGITE SUA SENHA:", type="password", disabled=st.session_state.desabilitar)

if st.button("VERIFICAR"):
    if login == usuario1 and senha == senha1:
        st.success("BEM VINDO!")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:
            st.warning(f"Login ou senha inválidos, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True
            st.error("Número de tentativas inválida.")
