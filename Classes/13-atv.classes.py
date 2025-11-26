import os
os.system("cls")

from dataclasses import dataclass

@dataclass 
class Funcionario:
    nome: str
    data_de_adm: int
    matricula: int
    endereco: str
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nData de admissão: {self.data_de_adm}\nMatrícula: {self.matricula}\nEndereço: {self.endereco}\n")

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: int
    endereco: str
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nData de nascimento: {self.data_de_nascimento}\nEndereço: {self.endereco}\n")

lista_funcionarios = []
lista_clientes = []

QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3


for i in range(QUANTIDADE_FUNCIONARIOS):
    print(f"\n=== FUNCIONÁRIO {i+1} ===")
    funcionario = Funcionario(
        nome=input("Informe o nome: "),
        data_de_adm=input("Informe data de admissão: "),
        matricula=input("Informe o número de matrícula: "),
        endereco=input("Informe o endereço: ")
    )
    lista_funcionarios.append(funcionario)


for i in range(QUANTIDADE_CLIENTES):
    print(f"\n=== CLIENTE {i+1} ===")
    cliente = Cliente(
        nome=input("Informe o nome: "),
        data_de_nascimento=input("Informe a data de nascimento: "),
        endereco=input("Informe o endereço: ")
    )
    lista_clientes.append(cliente)

arquivo_nome = "dados_paciente.csv"


try:
    with open(arquivo_nome, "a") as arquivo:
        arquivo.write("FUNCIONARIOS:\n")
        for f in lista_funcionarios:
            arquivo.write(f"============================\nNome:{f.nome} \nData de admissao: {f.data_de_adm}\n Matricula: {f.matricula} Endereco: {f.endereco}\n")

        arquivo.write("\nCLIENTES:\n")
        for c in lista_clientes:
            arquivo.write(f"============================\nNome: {c.nome}\nData de nascimento: {c.data_de_nascimento}\nEndereco: {c.endereco}\n")
    print("\nDados salvos com sucesso!")

except Exception as e:
    print(f"Erro ao salvar os dados no arquivo: {e}")


print("\n=== DADOS DOS FUNCIONÁRIOS ===")
for funcionario in lista_funcionarios:
    funcionario.exibir_dados()


print("\n=== DADOS DOS CLIENTES ===")
for cliente in lista_clientes:
    cliente.exibir_dados()

