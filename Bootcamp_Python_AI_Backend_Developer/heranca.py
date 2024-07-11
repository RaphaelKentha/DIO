#heranca erda as caracteristicas de uma classe para outra
#reaproveitamento de codigo
#classe A, transmite para a classe B, por consequencia a C herda de B 
# que herdou de A

#heranca simples
class A:
    pass
class B(A):
    pass
#exemplo de heranca simples

#heranca multipla, e quando uma classe herda de mais de uma classe
class A:
    pass
class B:
    pass
class C(A,B):
    pass
#class C herda de A e B

#exemplo heranca simples
class Veiculo:
    def __init__(self,modelo,ano,cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def __str__(self):
        return f'{self.modelo} {self.ano} {self.cor}'
    def ligar(self):
        print('Veiculo ligado')

class Carro(Veiculo):
    pass

carro1 = Carro('Fusca', 1975, 'Azul')
print(carro1)
carro1.ligar()
#observe que a classe carro herda de veiculo, e nao precisa de um metodo __init__ para carro
#pois ele herda de veiculo, e o metodo __str__ tambem e herd
#o metodo ligar tambem e herdado

class Caminhao(Veiculo):
    def __init__(self,modelo,ano,cor,carga):
        super().__init__(modelo,ano,cor)
        self.carga = carga
    
def carga(self):
    print(f"{'sim' if self.carga else 'nao'} esta carregado")

caminhao1 = Caminhao('Mercedes', 1990, 'Branco', True)
print(caminhao1)
caminhao1.ligar()

caminhao1 = Caminhao('Mercedes', 1990, 'Branco', True)
print(caminhao1)
caminhao1.ligar()
#o primeiro parametro do metodo __init__ e o self, que e a propria instancia
#sobrescrevendo o metodo __init__ da classe veiculo
#para manter a compatibilidade com a classe pai, usamos o super().__init__(modelo,ano,cor)

#heranca multipla
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {' , '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        #retorna o nome da classe e os atributos

class Mamifero(Animal):
    def __init__(self, pelos, **kw):
        super().__init__(**kw)
        self.pelos = pelos
        #herda de animal e adiciona o atributo pelos

class Ave(Animal):
    def __init__(self, penas, **kwargs):
        super().__init__(**kwargs)
        self.penas = penas
        #herda de animal e adiciona o atributo penas

class Ornitorrinco(Mamifero, Ave):
    pass

class Gato(Mamifero):
    pass
    
ornitorrinco = Ornitorrinco(pelos='macio', penas='brilhantes', nro_patas=4)
print(ornitorrinco)
print(ornitorrinco.__mro__)
#o metodo __mro__ mostra a ordem de heranca
gato = Gato(pelos='curto', nro_patas=4)
print(gato)
#devido a heranca multipla, a classe ornitorrinco herda de mamifero e ave
#e por causa do **kw, podemos passar os parametros para as classes pai
#mais teremos que passar de forma explicita, pois o python nao sabe para qual classe pai