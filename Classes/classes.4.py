import os
os.system("cls")


texto =  input("Digite seu nome: ")

nome_arquivo = "exemplo.txt"


with open(nome_arquivo, "a")as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("Salvo com sucesso!")