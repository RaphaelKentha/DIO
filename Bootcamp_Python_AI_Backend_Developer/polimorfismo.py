#polimorfismo e a capacidade de um objeto poder ser referenciado de varias formas
#exemplo: um objeto do tipo cachorro pode ser referenciado como um animal
#ou um objeto do tipo gato pode ser referenciado como um animal

len("teste") #funcao len() retorna o tamanho de uma string
len([1,2,3,4,5]) #funcao len() retorna o tamanho de uma lista
#para cada objeto, a funcao len() retorna um valor diferente,
#se comportando de forma diferente para cada objeto

#polimorfismo com heranca

class Passaro:
    def voar(self):
        print("Voando")

class Pato(Passaro):
    def voar(self):
        super().voar()
        #usando o super() para chamar o metodo da classe pai

class Galinha(Passaro):
    def voar(self):
        print("Galinha nao voa")
#implementacao da heranca


def voo(obj):
    obj.voar()
#como o objeto recebe um tipo passaro, ele voa, pois a funcao voar() esta implementada em passaro

passaro1 = Pato()
passaro2 = Galinha()

voo(passaro1)
voo(passaro2)