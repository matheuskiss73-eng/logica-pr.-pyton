import os
os.system("cls")

def saudacao(nome, idade, Peso, altura):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"sua idade é {idade} anos.")
    print(f"Você pesa {Peso}kg")
    print(f"Você tem {altura:.2f} de altura")


print("Solicitando dados")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
Peso = float(input("Digite sua peso: "))
altura = float(input("Digite sua altura: "))

saudacao(nome, idade, Peso, altura)