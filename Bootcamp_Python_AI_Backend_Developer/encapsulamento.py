#encapsular é proteger o código, proteger o código de ser acessado por outros códigos
#encapsulamento é um dos pilares da programação orientada a objetos (POO)
#encapsulamento é o ato de encapsular os atributos de uma classe, ou seja, proteger os atributos de uma classe

#recursos publicos e privados
#publico: acessivel por qualquer classe
#privado: acessivel apenas pela classe que o criou (atributos e métodos)
# __atributo = privado (dois underlines)
# __metodo() = privado (dois underlines)

class Conta:
    def __init__(self, saldo = 0, nro_agencia = 0, nro_conta = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia #atributo publico
        self._nro_conta = nro_conta
    
    def deposito(self, valor):
        self._saldo += valor
    
    def saque(self, valor):
        self._saldo -= valor

#o metodo __init__ é um metodo construtor, ele é chamado automaticamente quando um objeto é instanciado
#e ele e privado dessa classe
#metodo sacar e depositar são publicos, pois em um sistema bancario faz sentido que o usuario possa sacar e depositar
#e no caso de qualquer coisa que faca um extrato, o saldo é privado, pois não faz sentido que o usuario possa alterar o saldo

conta = Conta(100)
print(conta._saldo) #erro, pois o saldo é privado
#a saida funciona, etretanto vai contra as boas praticas de programação em python

#propertys são metodos que permitem acessar e alterar atributos privados

class Foo:
    def __init__(self, x = None):
        self._x = x
        #inicializa o atributo privado _x

    @property
    def x(self):
        return self._x or 0
        #retorna o valor do atributo privado _x
        #@property é um decorador que transforma o metodo 
        #em uma propriedade

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
        #altera o valor do atributo privado _x
        #@x.setter é um decorador que transforma o metodo
        #em um metodo setter

    @x.deleter
    def x(self):
        self._x = -1
        #deleta o valor do atributo privado _x
        #@x.deleter é um decorador que transforma o metodo
        #em um metodo deleter
        #o metodo deleter é chamado quando o atributo é deletado
        #mas pode alterar o funcnamento do restante do código que esta
        #usando o atributo

foo = Foo(10)
#instancia a classe Foo com o valor 10
print(foo.x) #10
#imprime o valor do atributo privado _x
foo.x = 20
#altera o valor do atributo privado _x
print(foo.x) #30
#imprime o valor do atributo privado _x após a alteração
del foo.x
#deleta o valor do atributo privado _x
print(foo.x) #-1
