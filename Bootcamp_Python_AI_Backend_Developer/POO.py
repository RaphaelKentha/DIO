#paradigma de programacion orientada a objetos
#conceitos basicos de POO: classes, objetos, atributos, metodos, construtores, heranca, polimorfismo, encapsulamento
#classes e objetos

#definindo uma classe
class Gato:
    #construtor
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor

    #metodo
    def miar(self):
        print("miau miau miau")

    def dormir(self):
        print("zzzzzzzzzzzz")

gato1 = Gato("Tom", 3, "preto")
gato2 = Gato("Felix", 5, "branco")
gato1.miar()
gato2.dormir()
#definindo a classe gato, com os atributos nome, idade e cor
#criando um objeto da classe gato, chamado gato1 e gato2
#chamando o metodo miar do objeto gato1 e o metodo dormir do objeto gato2

#desafio POO: jaesus tem uma loja de bicicletas e gostaria de 
#registra as biciletas em estoque e as vendidas

class Bicicleta:
    def __init__(self, ano, marca, modelo, cor, preco):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def exibir_bicicleta(bicicleta):
        print("Ano: ", bicicleta.ano)
        print("Marca: ", bicicleta.marca)
        print("Modelo: ", bicicleta.modelo)
        print("Cor: ", bicicleta.cor)
        print("Preco: ", bicicleta.preco)

    def buzinando(self):
        print("buzinando")

    def freando(self):
        print("freando")

    def pedalando(self):
        print("pedalando")

bicicleta1 = Bicicleta(2020, "Caloi", "Elite", "vermelha", 1000)

bicicleta1.exibir_bicicleta()
bicicleta1.pedalando()
bicicleta1.buzinando()
bicicleta1.freando()

#constructores
#metodos especiais que sao chamados automaticamente quando um objeto da classe e criado
#metodo __init__ e um construtor que e chamado automaticamente quando um objeto da classe e criado

class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print("au au au")

    def __del__(self):
        print("Objeto Cachorro foi excluido")
        #o pyutho ja exclui o objeto automaticamente, 
        # #mas e possivel adicionar um metodo destructor para liberar recursos antes de excluir o objeto

#metodo destructor
#metodo __del__ e um metodo destructor que e chamado automaticamente quando um objeto da classe e excluido
#destrutor e usado para liberar recursos antes de excluir um objeto

cachorro1 = Cachorro("Rex", "Pastor Alemao")
cachorro1.latir()