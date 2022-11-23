# Faça um Programa que leia um vetor de 10 números reais e
# mostre-os na ordem inversa.

lista = [9, 8, 76, 3, 2, 6, 7, 8, 2, 3, 4, 1]

for numero in reversed(lista):
    print(numero)
# ou 
lista.reverse()
print(lista)