# Criando um Sistema Bancário com Python
'''
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
-> depósito: adicionar dinheiro à conta
-> saque: retirar dinheiro da conta
    --> cada saque tem o limite de 500 reais
    --> o saldo da conta não pode ser negativo
    --> limitado a 3 saques por dia
-> extrato: mostrar o saldo da conta
    --> mostra os saques e depósitos realizados,em ordem cronológica
'''

def deposito(valor, saldo, extrato):
    saldo += valor
    extrato.append(f'Depósito: R$ {valor:.2f}')
    return saldo

def saque(valor, saldo, extrato, saques):
    if valor > 500:
        print('O valor máximo para saque é de R$ 500')
    elif saldo < valor:
        print('Saldo insuficiente')
    elif saques == 3:
        print('Limite de saques diários atingido')
    else:
        saldo -= valor
        extrato.append(f'Saque: R$ {valor:.2f}')
        saques += 1
    return saldo, saques

def extrato_bancario(saldo, extrato):
    print(f'Saldo: R$ {saldo:.2f}')
    print('Extrato:')
    for operacao in extrato:
        print(operacao)

operacao = ''
print('Bem-vindo ao Banco Python')
saldo = 0
extrato = []
saques = 0
print('Operações disponíveis: \n1 - depósito\n2 - saque\n3 - extrato\n4 - sair')
while operacao != '4':
    operacao = input('Digite o número da operação desejada: ')
    if operacao == '1':
        valor = float(input('Digite o valor do depósito: '))
        saldo = deposito(valor, saldo, extrato)
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso')
        print(f'Desaja realizar outra operação?')
        if input('Digite "S" ou "N": ').lower() == 'n':
            operacao = '4'
    elif operacao == '2':
        valor = float(input('Digite o valor do saque: '))
        saldo, saques = saque(valor, saldo, extrato, saques)
        print(f'Saque de R$ {valor:.2f} realizado com sucesso')
        print(f'Desaja realizar outra operação?')
        if input('Digite "S" ou "N": ').lower() == 'n':
            operacao = '4'
    elif operacao == '3':
        extrato_bancario(saldo, extrato)
        print(f'Desaja realizar outra operação?')
        if input('Digite "S" ou "N": ').lower() == 'n':
            operacao = '4'
    elif operacao == '4':
        print('Obrigado por utilizar o Banco Python')
    else:
        print('Operação inválida')