import os
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    idade: int
    cpf: str
@dataclass
class pet:
    nome: str
    idade: int
    peso: float


#exemplo de uso da classe
pessoa1 = pessoa(nome= "alice",cpf="1234567890",idade=30)
pet1 = pet(nome="bob", idade=2, peso=5)

print("pessoa: ")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}\n")
print("pet: ")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso}")