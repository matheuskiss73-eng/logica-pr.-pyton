import os
os.system("cls")
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    cpf: str
    telefone: str
    
    def mostrar_dados(self):
        print("=======================================")
        print("Solicitação de Dados: ")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        

    def dados_sms_marketing(self):
        print("=======================================")
        print("Solicitação de Dados: ")
        print(f"Telefone: {self.telefone}")
        



print("Solicitando os dados")
lista_pessoas = []
for i in range(2):
    pessoa1 = pessoa(nome=input("Digite o seu nome: "),    
                cpf=input("Digite o seu CPF: "),
                telefone=input("Digite a sua Telefone: "))
    lista_pessoas.append(pessoa1)

os.system("cls")
print("Solicitação de Dados: ")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()
print("=======================================")
for pessoa in lista_pessoas:
    pessoa.dados_sms_marketing()