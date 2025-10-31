import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Autor:
    nome : str
    biografia: str


@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    
    
    def exibir_detalhes(self):
        os.system("cls")
        print("===Exibindo Dados do livro ===")
        print(f"Titulo: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Nome do Autor: {self.autor.nome}, {self.autor.biografia}")
    
Autor1 = Livro(
    titulo=input("Digite o titulo do livro: "),
    ano=int(input("Digite o Ano de publicação: ")),
    autor=Autor(nome= input("Digite o nome do autor: "),
    biografia = input("Digite a biografia: "))
 
)


Autor1.exibir_detalhes()