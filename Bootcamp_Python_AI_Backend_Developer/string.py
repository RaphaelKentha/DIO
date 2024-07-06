#string
exemple = "Bonjour"
print(exemple) #imprime o conteudo da variavel exemple
print(exemple.upper()) #imprime o conteudo da variavel exemple em maiusculas
print(exemple.lower()) #imprime o conteudo da variavel exemple em minusculas
print(exemple.capitalize()) #imprime o conteudo da variavel exemple com a primeira letra em maiuscula
print(exemple.strip()) #imprime o conteudo da variavel exemple sem os espacos em branco
print(exemple.replace("o", "a")) #imprime o conteudo da variavel exemple substituindo a letra "o" pela letra "a"
print(exemple.rstrip()) #imprime o conteudo da variavel exemple sem os espacos em branco a direita
print(exemple.lstrip()) #imprime o conteudo da variavel exemple sem os espacos em branco a esquerda
print(exemple.center(20)) #imprime o conteudo da variavel exemple centralizado em 20 caracteres
print(exemple.ljust(20)) #imprime o conteudo da variavel exemple justificado a esquerda em 20 caracteres
print(exemple.rjust(20)) #imprime o conteudo da variavel exemple justificado a direita em 20 caracteres
print(".".join(exemple)) #imprime o conteudo da variavel exemple com um ponto entre cada letra

#formatacao
nome = "Maria"
idade = 30
print(f"Ola, meu nome e {nome} e tenho {idade} anos") #imprime o conteudo das variaveis nome e idade na frase

#formatacao de numeros com f strings
numero = 10.5432
print(f"O numero e {numero:.2f}") #imprime o conteudo da variavel numero com 2 casas decimais

#fatiamento de strings
frase = "O rato roeu a roupa do rei de Roma"
print(frase[2]) #imprime a terceira letra da frase
print(frase[2:6]) #imprime da terceira a sexta letra da frase
print(frase[::-1]) #imprime a frase de tras para frente

#strind de multiplas linhas
# comentario com """ xxxxxx """