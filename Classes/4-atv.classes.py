import os
os.system("cls")
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    email: str
    endereco: str
    
    def mostrar_sados(self):
        print("Solicitação de Dados: ")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")
        

    def mostrar_somente_nome(self):
        print("Solicitação de Dados: ")
        print(f"Nome: {self.nome}")
        



print("Solicitando os dados")
lista_pessoas = []
for i in range(2):
    pessoa1 = pessoa(nome=input("Digite o seu nome: "),    
                endereco=input("Digite o seu Endereço: "),
                email=input("Digite a sua Email: "))
    lista_pessoas.append(pessoa)

os.system("cls")
print("Solicitação de Dados: ")
for pessoa in lista_pessoas:
    pessoa.mostrar_sados()
print("=======================================")
for pessoa in lista_pessoas:
    pessoa.mostrar_somente_nome()
