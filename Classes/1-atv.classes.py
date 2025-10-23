import os
os.system("cls")
from dataclasses import dataclass
@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float



print("solicitando os dados da pessoa")
pessoa1 = pessoa(
    nome=input("Digite o seu nome: "),    
    peso=float(input("Digite o seu peso: ")),   
    idade=int(input("Digite a sua idade: ")), 
    altura=float(input("Digite a sua altura: ")))

import os
os.system("cls")
print("Dados da pessoa: ")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}")
