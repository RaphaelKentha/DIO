# Dicionário
# Um dicionário é uma coleção de pares chave-valor

pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
dict1 = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}

# Criando o mesmo dicionário de duas formas diferentes
pessoa["telefone"] = "5521999999999"  # Adicionando um novo par chave-valor no dicionário pessoa
print(pessoa)
print(dict1)

# Acessando o conteúdo do dicionário
print(pessoa['nome'])  # Prof. Alberto
print(pessoa['idade'])  # 43
print(pessoa['cursos'])  # ['React', 'Python']

# Alterando o conteúdo de um par chave-valor
pessoa['idade'] = 44  # Alterando a idade de 43 para 44
print(pessoa)

# Dicionários aninhados
contatos = {'albert': {'nome': 'Prof. Alberto', 'idade': 43},
            'ana': {'nome': 'Ana', 'idade': 22},
            'wesley': {'nome': 'Wesley', 'idade': 35}}

# Acessando o conteúdo de um dicionário aninhado
print(contatos['albert'])  # {'nome': 'Prof. Alberto', 'idade': 43}
print(contatos['albert']['nome'])  # Prof. Alberto

# Iterações com dicionários
for contato in contatos:
    print(contato)

# Acessando o conteúdo de um dicionário aninhado
for chave, valor in contatos.items():
    print(chave, valor)

# Métodos de dicionários
# Método get() retorna o valor de uma chave; se a chave não existir, retorna None
print(pessoa.get('idade'))  # 44
print(pessoa.get('tags'))  # None
print(pessoa.get('tags', []))  # []

# Método fromkeys() cria um dicionário com as chaves passadas e um valor padrão
usuarios = {}.fromkeys(['nome', 'idade', 'email', 'profile'], 'desconhecido')
print(usuarios)

# Método pop() remove um par chave-valor de um dicionário
print(pessoa.pop('idade'))  # 44

# Métodos items(), keys() e values()
print(contatos.items())
print(contatos.keys())
print(contatos.values())

# Método update() atualiza um dicionário com outro dicionário
pessoa.update({'idade': 43, 'sexo': 'M'})
print(pessoa)

# Método copy() copia um dicionário
pessoa2 = pessoa.copy()
print(pessoa2)

# Método popitem() remove um par chave-valor aleatório de um dicionário
print(pessoa.popitem())
print(pessoa)

# Método setdefault() retorna o valor de uma chave; se a chave não existir, insere a chave com o valor (opcional)
print(pessoa.setdefault('tags', []))

# Método in verifica se uma chave existe no dicionário
print('tags' in pessoa)  # True
print('tags' in pessoa2)  # False

# Método len() retorna o número de itens de um dicionário
print(len(pessoa))
print(len(pessoa2))

# Método del() deleta um item de um dicionário
del pessoa['tags']
