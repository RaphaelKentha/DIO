#listas
para_lista = []
para_lista.append(input("Digite o primeiro nome: "))
print(para_lista)

letra_separadas = list(para_lista[0])
#adicio a letra separada o elemento 0 da lista para_lista
# em letras separadas
print(letra_separadas)

lista_fatiada = letra_separadas
print(lista_fatiada)
print(lista_fatiada[0::-1]) #fatiando a lista

#filtro
numero = [1,2,3,4,5,6,7,8,9,10]
pares = []
print(numero)
for aux in numero:
    if aux % 2 == 0:
        pares.append(aux)
print(pares)

#filtro 2 - one line
impares = [aux for aux in numero if aux % 2 != 0] #list comprehension, numero impares
print(impares)

#metodos da lista
'''
.append() - adiciona um elemento no final da lista
.insert() - adiciona um elemento em uma posição específica
.pop() - remove o último elemento da lista
.remove() - remove um elemento específico da lista
.clear() - remove todos os elementos da lista
.sort() - ordena a lista
.reverse() - inverte a ordem da lista
.copy() - copia a lista
.count() - conta quantas vezes um elemento aparece na lista
.index() - retorna o índice de um elemento na lista
.extend() - adiciona os elementos de uma lista em outra
'''