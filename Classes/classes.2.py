import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    
    
    
@dataclass
class cliente:
    nome: str
    endereco: Endereco
    
    
cliente1 = cliente(nome="Marta",
                   endereco=Endereco(logradouro="Rua A",numero=23))


print("Mostrar dados do cliente.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco.logradouro}")
print(f"Número: {cliente1.endereco.numero}")