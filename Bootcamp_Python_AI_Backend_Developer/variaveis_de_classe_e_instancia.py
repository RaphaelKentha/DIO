#atributos de classe são atributos que são declarados diretamente na classe, fora de qualquer método.

class Estudante:
    escola = "DIO"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos e estuda na escola {self.escola}"
    
def mostra_valores(*objs):
    for objeto in objs:
        print(objeto)
        #funcao que recebe uma quantidade variavel de objetos e imprime os valores dos atributos de cada objeto.

estudante1 = Estudante("Pedro", 20)
estudante2 = Estudante("Maria", 30)
mostra_valores(estudante1, estudante2)

#a diferenca e que o atributo escola e um atributo de classe, ou seja, ele e compartilhado por todos os objetos da classe Estudante.
#ja os atributos nome e idade sao atributos de instancia, ou seja, cada objeto da classe Estudante tem seus proprios valores para esses atributos.
#veja que ao criar/modificar os dados de um objeto, isso nao afeta os dados de outro objeto.

estudante1 = Estudante("Pedro", 201)
estudante2 = Estudante("Maria", 301)

Estudante.escola = "DIO2"
#muda o valor do atributo de classe escola para DIO2
estudante3 = Estudante("Joao", 40)
mostra_valores(estudante1, estudante2, estudante3)

#metodos de classe e metodos estaticos
#metodos de classe sao metodos que sao declarados com o decorador @classmethod e recebem como primeiro parametro a propria classe.
#um metodo de classe pode acessar e modificar os atributos de classe,
#o metodo estatico nao modifica nem acessa os atributos da classe, ele e um metodo que nao recebe a classe como parametro e nao acessa os atributos da classe.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, nome, ano_nascimento):
        return cls(nome, 2021 - ano_nascimento)
    
    @staticmethod
    def is_adulto(idade):
        return idade >= 18
    #metodo estatico que recebe a idade de uma pessoa e retorna True se ela for maior de idade e False caso contrario.
    
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos"
    
pessoa1 = Pessoa("Pedro", 20)
pessoa2 = Pessoa.criar_data_nascimento("Maria", 1990)
mostra_valores(pessoa1, pessoa2)
print(Pessoa.is_adulto(20)) #retorna True

#classes abstratas
#uma classe abstrata e uma classe que nao pode ser instanciada, ou seja, nao podemos criar objetos dessa classe.
#interfaces sao classes abstratas que contem apenas metodos abstratos, ou seja, metodos que nao possuem implementacao.
#denine o que os metodos devem fazer, mas nao como eles devem fazer.

#criando classes abstratas com o modulo abc
from abc import ABC, abstractmethod

class Controle:
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class ControleRemoto(Controle):
    def ligar(self):
        print("Ligando o controle remoto")
    def desligar(self):
        print("Desligando o controle remoto")
    # o @abstractmethod obriga as classes filhas a implementarem os metodos ligar e desligar.

controle = ControleRemoto()
controle.ligar()
controle.desligar()