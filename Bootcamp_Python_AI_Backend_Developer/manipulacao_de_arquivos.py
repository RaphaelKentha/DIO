#manipulacao de arquivos(csv e txt)
#abertura e fechanmento de arquivos
# open() abre o arquivo
# close() fecha o arquivo
#modos de abertura de arquivos
# r - leitura
# w - escrita
# a - leitura e escrita
# b - modo binario
'''
arquivo = open('arquivo.txt', 'w')
#abrinto o arquivo para escrita
close = arquivo.close()
'''

#metodo read() - leitura de arquivos
'''
arquivo = open('arquivo.txt', 'r')
print(arquivo.read())
arquivo.close()
'''
arquivo = open("C:/Users/Kentha/Documents/GitHub/DIO/Bootcamp_Python_AI_Backend_Developer/zenpy.txt","r") 
#print(arquivo.read())
#print(arquivo.readline())
#retorna uma linha do arquivo
#print(arquivo.readlines())
#retorna uma lista com todas as linhas do arquivo


while len(linha := arquivo.readline()):
    print(linha, end='')
#leitura de arquivo com while
arquivo.close()

#escrevendo em arquivos Write()
arquivo = open("C:/Users/Kentha/Documents/GitHub/DIO/Bootcamp_Python_AI_Backend_Developer/zenpy.txt","w")
arquivo.write("Novo conteudo")
#sobrescreve o conteudo do arquivo
arquivo.writelines(["\n","Novo conteudo 2"])
#escreve uma lista de conteudo no arquivo
arquivo.close()


