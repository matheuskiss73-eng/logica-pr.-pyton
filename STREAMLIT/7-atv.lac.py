import streamlit as st

st.title("MÉDIA")

notas = []
for i in range(3):
    nota = st.number_input(f"Informe a {i+1}º nota:", min_value=0.0, max_value=10.0, step=0.1)
    notas.append(nota)

if st.button("Calcular sua média"):
    soma = sum(notas)
    media = soma / 3
    st.write(f"SUA MÉDIA É: {media:.2f}")

    if media >= 7:
        st.write(f"A sua média é {media:.2f}: VOCÊ FOI APROVADO. PARABÉNS!!!")
    elif 4.1 <= media < 7:
        st.write(f"A sua média é {media:.2f}: VOCÊ ESTÁ DE RECUPERAÇÃO.")
    else:
        st.write(f"A sua média é {media:.2f}: VOCÊ FOI REPROVADO.")
