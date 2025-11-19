import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: str
    
    def exibir_dados(self):
        print(f"Nome:{self.nome} \n Idade:{self.idade} \n Peso:{self.peso} \n Altura:{self.altura} \n CPF:{self.cpf} ")


lista_de_pacientes1=[]
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente=Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite seu idade: ")),
        peso= float(input("Digite seu peso: ")),
        altura= float(input("Digite seu altura: ")),
        cpf= input("Digite sua cpf: ")
    )
    lista_de_pacientes1.append(paciente)
    print() # Pular uma linha.
nome_do_arquivo = "dados_pacientes1.csv"
with open (nome_do_arquivo, "a") as arquivo_pacientes1:
    for paciente in lista_de_pacientes1:
        arquivo_pacientes1.write(f"===============================\n Nome:{paciente.nome}\n Idade: {paciente.idade} \n Peso: {paciente.peso} \n Altura: {paciente.altura} \n CPF: {paciente.cpf}\n")
        print("Dados salvos com sucesso.")
        
#print("\nExibindo lista de pacientes:")
#for paciente in lista_de_pacientes1:
#    paciente.exibir_dados()
    

print("\nExibindo todos os pacientes: ")
lista=[]
try:
    # "r" - read - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        #recebendo todos os dados de uma so vez
        lista_tds_pacientes = arquivo.readline()
        for paciente in lista_tds_pacientes:
            nome, idade, peso, altura,cpf = paciente.strip().strip(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade))
            lista.append(dados_paciente)
    for paciente in lista:
            paciente.exibir_dados
except FileNotFoundError:
    print("o arquivo não foi encontrado")