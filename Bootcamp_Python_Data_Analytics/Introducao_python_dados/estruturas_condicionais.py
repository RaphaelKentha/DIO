# Estruturas condicionais
# if, elif, else

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
'''	
4.1. Comandos if
Provavelmente o mais conhecido comando de controle de fluxo é o if. Por exemplo:
Pode haver zero ou mais partes elif, e a parte else é opcional. A palavra-chave ‘elif’ é uma 
abreviação para ‘else if’, e é útil para evitar indentação excessiva. Uma sequência 
if … elif … elif … substitui os comandos switch ou case, encontrados em outras linguagens.
Se você está comparando o mesmo valor com várias constantes, ou verificando por tipos ou atributos específicos, 
você também pode achar a instrução match útil. Para mais detalhes veja Instruções match.
'''	