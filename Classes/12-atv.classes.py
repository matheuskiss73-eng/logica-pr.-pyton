import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    data: str
    rg: str
    cpf: str
    
    def exibir_dados(self):
        print(f"Nome:{self.nome} \n Data  de nascimento:{self.data} \n RG:{self.rg} \n CPF:{self.cpf}")

lista_de_usuario1=[]
QUANTIDADE_DE_USUARIOS = 5

for i in range(QUANTIDADE_DE_USUARIOS):
    usuario=Usuario(
        nome= input("Digite seu nome: "),
        data= input("Digite sua Data  de nascimento: "),
        rg= input("Digite seu RG: "),
        cpf= input("Digite sua cpf: ")
    )
    lista_de_usuario1.append(usuario)
    print() # Pular uma linha.
nome_do_arquivo = "Funcionarios.csv"
with open (nome_do_arquivo, "a") as Funcionarios:
    for usuario in lista_de_usuario1:
        Funcionarios.write(f"{usuario.nome},{usuario.data},{usuario.rg},{usuario.cpf}\n")
        print("Dados salvos com sucesso.")
        

print("\nExibindo todos os usuario: ")
lista=[]
try:
    with open(nome_do_arquivo, "r") as arquivo:
        lista_tds_usuario = arquivo.readline()
        for usuario in lista_tds_usuario:
            nome, data, rg, cpf = usuario.strip().strip(",")
            dados_usuario = Usuario(
                nome=nome,
                data=data,
                rg=rg,
                cpf=cpf
            )
            
            lista.append(dados_usuario)
    for usuario in lista:
            usuario.exibir_dados()
except FileNotFoundError:
    print("o arquivo não foi encontrado")
    






#esse codigo nao esta 100% funcional, corrija