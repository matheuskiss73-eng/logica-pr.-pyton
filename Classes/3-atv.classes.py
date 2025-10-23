import os
os.system("cls")
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    idade: int
    
    def mostrar_dadods(self):
        print("Dados da pessoa: ")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")



print("Solicitando os dados da pessoa")
pessoa1 = pessoa(
    nome=input("Digite o seu nome: "),    
    idade=int(input("Digite o seu idade: ")))
print("=======================================")
pessoa2 = pessoa(
    nome=input("Digite o seu nome: "),    
    idade=int(input("Digite a sua idade: ")))


os.system("cls")
pessoa1.mostrar_dadods()
print("=======================================")
pessoa2.mostrar_dadods()