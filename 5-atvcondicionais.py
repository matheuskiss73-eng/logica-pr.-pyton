import streamlit as st

st.title("BOLETIM")


media =  st.number_input("digite a media: ")

if st.button("verificar"):
    if media  >= 7:
        st.success("aprovado!")
    else:
         st.warning("reprovado!")
    
else:
        st.info("INFORME A MÉDIA.")