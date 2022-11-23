# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.


def multiplicar(minha_lista):
    result = 1
    for i in minha_lista:
        result = result * i
    return result


def somar(minha_lista):
    result = 0
    for i in minha_lista:
        result = result + i
    return result


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Multiplicação de todos os números: {multiplicar(lista)}\nSoma de todos os números: {somar(lista)}\nNúmeros da lista base: {lista}')
