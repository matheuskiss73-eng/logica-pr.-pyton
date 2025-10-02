# verifique a idade de uma pessoa
# se menor que 18, mostre: menor de idade
# caso contrario, mostre maior de idade
# usando streamlit.

import streamlit  as st

st.title(" verificação de idade")

idade = st.number_input("informe sua idade: ", min_value=0, max_value=100, step=1)

if  st.button("verificar"):
    if idade < 18:
        st.write("menor de idade")
    else:
        st.write("maior de idade")


else:
    st.warning("por gentileza, digite sua idade.")