#funcoes sao blocos de codigo que sao executados quando chamados
#funcoes podem receber parametros e retornar valores
#funcoes sao definidas com a palavra reservada def

def exibir_mensagem():
    print("Ola, seja bem-vindo ao py!")
#chamando a funcao
exibir_mensagem()

#funcoes podem receber parametros
def exibir_nome(nome):
    print(f"Ola, {nome}!")
#chamando a funcao
exibir_nome("Lucas") #passando o argumento "Lucas" para a funcao

#funcoes podem retornar valores por def
def exibir_nome2(nome="Desconhecido"):
    print(f"Ola, {nome}!")
#chamando a funcao
mensagem = exibir_nome2()
#caso nao seja passado nenhum argumento, o valor padrao sera "Desconhecido"

#dado que temos uma lista:
def soma_lista(lista_numeros):
    return sum(lista_numeros)

lista = [1, 2, 3, 4, 5]
resultado = soma_lista(lista) #resultado = 15
print(resultado)

def numero_antecessor_sucessor(numero):
    return numero-1, numero+1
#retorna uma tupla com o antecessor e o sucessor do numero passado como argumento
numero_antecessor_sucessor(5) #retorna (4, 6)
print(numero_antecessor_sucessor(5))

def salvar_carro(carro, marca, ano):
    print(f"Carro: {carro}, Marca: {marca}, Ano: {ano}")
#podemos passar os argumentos de forma explicita
salvar_carro(carro="Civic", marca="Honda", ano=2005)
#ou de forma implicita
salvar_carro("Civic", "Honda", 2005)
salvar_carro(**{"carro": "Civic", "marca": "Honda", "ano": 2005})
#podemos passar os argumentos de forma explicita usando um dicionario

# args e kwargs, args recebe uma tupla e kwargs recebe um dicionario
def exibir_poema(data_extenso, *args, **kwargs):
    # Junta os elementos da tupla args com uma quebra de linha
    texto = "\n".join(args)
    
    # Cria uma string com os metadados (chave: valor) a partir do dicionário kwargs
    meta_dados = "\n".join(f"{chave}: {valor}" for chave, valor in kwargs.items())
    
    # Imprime o poema formatado
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# Exemplo de uso da função
exibir_poema("sexta feira 13", "zen of python", "beautiful is better than ugly", "explicit is better than implicit", "simple is better than complex", autor="Tim Peters", ano=2004)

#parametros especiais
def criar_carro(modelo, ano, placa, / , marca, motor, combustivel, *, cor):
    print(f"Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Marca: {marca}, Motor: {motor}, Combustivel: {combustivel}, Cor: {cor}")
#na funcao acima, os parametros modelo, ano e placa sao posicionais, ou seja, devem ser passados na ordem
#os parametros marca, motor e combustivel sao posicionais ou nomeados, ou seja, podem ser passados na ordem ou explicitamente
#o parametro cor e obrigatorio e deve ser passado explicitamente

criar_carro("Civic", 2005, "ABC-1234", marca="Honda", motor="1.8", combustivel="Gasolina", cor="Preto")
#os parametros modelo, ano e placa sao passados de forma posicional
#os parametros marca, motor e combustivel sao passados de forma explicita
#o parametro cor e passado de forma explicita
criar_carro("Civic", 2005, "ABC-1234", "Honda", "1.8", "Gasolina", cor="Preto")
#note que os parametros marca, motor e combustivel sao passados de forma posicional neste caso
#pois os mesmos nao possuem o marcador / na definicao da funcao

#keyword-only arguments
def exibir_informacoes(*, nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")
#os parametros nome e idade sao obrigatoriamente passados de forma explicita
exibir_informacoes(nome="Lucas", idade=25)

#keyword-only arguments com parametros posicionais
def exibir_informacoes2(nome, sexo, /, *, idade, cidadania):
    print(f"Nome: {nome}, Sexo: {sexo}, Idade: {idade}, Cidadania: {cidadania}")
#os parametros nome e sexo sao passados de forma posicional
#os parametros idade e cidadania sao passados de forma explicita
exibir_informacoes2("Lucas", "M", idade=25, cidadania="Brasileiro")

#objetos de primeira classe
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def exibir_resultado(funcao, a, b):
    return funcao(a, b)
    print(f"Resultado: {funcao(a, b)}")
#podemos passar uma funcao como argumento para outra funcao
resultado = exibir_resultado(soma, 5, 5) #resultado = 10
resultado2 = exibir_resultado(subtracao, 5, 5) #resultado2 = 0
print(resultado)
print(resultado2)

novo_nome_de_soma = soma
#podemos atribuir uma funcao a uma variavel
resultado3 = novo_nome_de_soma(5, 5) #resultado3 = 10
print(resultado3)

#escopo local e global
salario = 12
def bonus(salario):
    return salario * 0.1
#o salario passado como argumento e uma variavel local
#o salario fora da funcao e uma variavel global
bonus_salario = bonus(salario) #bonus_salario = 1.2
print(bonus_salario)
#nota usar variaveis globais dentro de funcoes e uma pratica ruim