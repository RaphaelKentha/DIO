#separador de vogais e consoantes
texto = input("Digite um texto: ")
vogais = "AEIOU"
armazena_vogais = ""
armazena_consoantes = ""

for aux in texto:
    if aux.upper() in vogais:
        armazena_vogais += aux
    elif aux == " ":
        continue
    else:
        armazena_consoantes += aux
print(f"Vogais: {armazena_vogais}")
print(f"Consoantes: {armazena_consoantes}")

for aux in range(1, 11):
    print(aux, end=" ")

while True:
    try:
        numero = int(input("\nDigite um número: "))
        break
    except ValueError:
        print("Digite um número inteiro")
# Este código cria um loop infinito que solicita ao usuário que insira um número inteiro.
# Se o usuário inserir algo que não pode ser convertido em um número inteiro,
# ele receberá a mensagem “Digite um número inteiro” e será solicitado a tentar novamente.
