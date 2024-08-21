# Recebe a lista do usuário
entrada = input()
# Converte a string de entrada em uma lista de números
lista = [int(x.strip()) for x in entrada.split(',')]

# Remova as duplicatas mantendo a ordem da última ocorrência
lista_unica = []
for x in reversed(lista):
    if x not in lista_unica:
        lista_unica.append(x)
lista_unica.reverse()

# É exibida a nova lista sem valores duplicados
print(lista_unica)

##########################################################################################

# Receber a lista do usuário
entrada = input()

# Converter a string de entrada em uma lista de valores
lista = [int(x.strip()) if x.strip().isdigit() else None for x in entrada.split(',')]

# TODO: Conte quantos elementos são None usando a função count:
contador_nulos = lista.count(None)

# Exibir o resultado
print(contador_nulos)