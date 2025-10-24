import os
os.system("cls")
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
    
    def mostrar_dados(self):
        print("=======================================")
        print("Solicitação de Dados: ")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print("=======================================")
        

print("Solicitando os dados")
lista_pessoas = []
for i in range(4):
    pessoa1 = pessoa(nome=input("Digite o seu nome: "),    
    peso=float(input("Digite o seu peso: ")),   
    idade=int(input("Digite a sua idade: ")), 
    altura=float(input("Digite a sua altura: ")))
    print("=======================================")
    lista_pessoas.append(pessoa1)

os.system("cls")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()
print("=======================================")