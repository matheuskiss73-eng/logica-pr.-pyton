import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print("===Dados da Pessoa ===")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, {self.endereco.numero} - {self.endereco.cidade}")


cliente1 = Cliente(
    nome=input("Digite o seu nome: "),
    email=input("Digite o seu email: "),
    endereco=Endereco(logradouro = input("Digite o seu logradouro: "),
numero = int(input("Digite o número: ")),
cidade = input("Digite a cidade: "))
)

cliente1.mostrar_dados()
