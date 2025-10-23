import os
os.system("cls")
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dadods(self):
        import os
        os.system("cls")
        print("Dados da pessoa: ")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Enderço: {self.endereco}")


print("Solicitando os dados da pessoa")
pessoa1 = pessoa(
    nome=input("Digite o seu nome: "),    
    email=input("Digite o seu Email: "),
    telefone=input("Digite a sua Telefone: "), 
    endereco=input("Digite a sua Enderço: "))


pessoa1.mostrar_dadods()
