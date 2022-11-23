# Metodo index
# Utilizado para encontrar a posição de um valor especificado:

lista = ['Carro', 'Casa', 'Hotel', 'Casa']
pos = lista.index('Casa')
print(f'O item desejado está na posição: {pos}')

print('-' * 40)

# Metodo Count
# O metodo count(elemento) retorna o numero de vezes que
# o valor especificado aparece na lista
pos = lista.count('Casa')
print(f'O item desejado aparece na lista {pos} vezes')

print('-' * 40)

# Metodo append
# Para adicionar um elemento ao final da lista use o metodo append(elemento)
lista = ['Python', 'Academy']
lista.append('Adicionado')
print(lista)

print('-' * 40)

# Metodo insert
# Para adicionar um item em um indice especificado,
# use o metodo insert(indice, elemento)
lista = ['Python', 'Academy']
lista.insert(0, 'Blog')
print(lista)

print('-' * 40)

# Metodo extend
# extend(iteravel) adiciona os elemntos de uma lista especificada
# Ou qualquer outro iteravel ao final da lista
sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']
# sacola.extend(legumes)
# print(sacola)

juntos = sacola + legumes
print(juntos)

print('-' * 40)

# E também podemos percorrer uma das listas, adicionando elementos à outra
# com o método append(), assim:

sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']
for legume in legumes:
    sacola.append(legume)
print(sacola)

print('-' * 40)

# Método remove
# Para remover um item com valor especificado,
# use o método remove(elemento):
lista = ['blog', 'python', 'academy']
lista.remove('blog')
print(lista)

print('-' * 40)

# Outra forma de remover elementos
# de uma lista é utilizando a função del do próprio Python, assim:
lista = [10, 20, 30, 40]
del lista[0]
print(lista)

print('-' * 40)

# Metodo Pop
# Para remover um item do indice especificado e ainda retorna-lo
# use o metodo pop(indice) dessa forma:
lista = ['Banana', 'Limao', 'Carro', 'Laranja']
item = lista.pop(2)
print(f'item: {item}')
print(f'Lista: {lista}')

print('-' * 40)

# Metodo Clear
# Esse metodo é utilizado para remover todos os elementos de uma lista dessa forma:
lista = [10, 20, 40, 50]
lista.clear()
print(lista)

print('-' * 40)

# Metodo copy
# Retorna uma copia da lista
lista = ['Python', 'Academy']
lista_copiada = lista.copy()
print(lista, lista_copiada)

print('-' * 40)

# Metodo reverse

lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

# Metodo sort
# Esse metodo é utilizado para ordenar listas.
# Tambem é possivel criar um afunção para definir seus proprios
# criterios de ordenação com sort(key=funcao)
print('-' * 40)

lista = [1, 2, 34, 5, 6, 77, 9, 453]
lista.sort()
print(lista)

# Adicionando o parâmetro reverse=True, é possível ordenar a lista em ordem decrescente.
#
# Para deixar do modo padrão basta colocar reverse=False:
lista = [1, 4, 5, 2, 4]

lista.sort(reverse=True)

print(lista)

print('-' * 40)
print('-' * 40)

# Keyword len()
# Retorna a quantidade de itens em uma lista, utilizando o método len(iterável):

lista = [10, 20, 30, 40, 50, 60]
print('A quantiade de itens na lista: ', len(lista))

print('-' * 40)

# keyword min()
# A função min(iteravel (devolve o item com menor valor da lista ou iteravel
# de entrada:
lista = [2, 4, 8, 1]
print('Menor valor da lista', min(lista))

# Keyword max()
# Retorne o maior valor da lista ou iterável especificado mix(iterável):
lista = [2, 4, 8, 1]
print('Maior valor da lista',
      max(lista))

print('-' * 40)

# Keyword reversed()
# A função reversed() reverte a ordem da lista de entrada

lista = [1,2,3,4,7]
for item in reversed(lista):
    print(item)