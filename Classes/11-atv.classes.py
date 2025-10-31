import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    autor: str
    categoria:str
    preço: float
    
QUANTIDADE_LIVROS = 3
lista_livros = []


print("Solicitando dados do aluno.")
for i in range (QUANTIDADE_LIVROS):
    print("=======================================")
    aluno = Aluno(
        nome= input("Digite o nome do livro: "),
        autor=input("Digite o nome do autor: "),
        categoria=input("Digite a categoria dele: "),
        preço= float(input("Digite o preço do livro: "))
       
    )
    lista_livros.append(aluno)
    
    
print()
print("Salvando dados.")
arquivo = "dados_livros.txt"

with open(arquivo, "a") as dados_livros:
    for aluno in lista_livros:
        dados_livros.write(
            f"============================\nNome do livro: {aluno.nome}\nNome do autor: {aluno.autor}\nCategoria: {aluno.categoria}\nPreço do livro: {aluno.preço}\n")
    print("Salvo com sucesso.")