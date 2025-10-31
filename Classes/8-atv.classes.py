import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        
        print("===Dados da Pessoa ===")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}, {self.endereco.numero}")


cliente1 = Cliente(
    nome=input("Digite o seu nome: "),
    idade=int(input("Digite a sua idade: ")),
    endereco=Endereco(logradouro = input("Digite o seu logradouro: "),
    numero = int(input("Digite o número: ")))

)

cliente1.mostrar_dados()
