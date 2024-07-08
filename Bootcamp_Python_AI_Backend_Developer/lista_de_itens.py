# Exibe a lista de itens
print("Lista de Equipamentos:")  
itens = []
for aux in range(0, 3):
    itens.append(input("digite a lista"))
    aux += 1
    # Loop que percorre cada item na lista "itens"
    print(f"- {itens}")