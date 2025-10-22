import os
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    idade: int

#exemplo de uso da classe
pessoa1 = pessoa("alice",30)
pessoa2 = pessoa("bob",25)


print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}")