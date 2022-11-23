# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

inteiros = []
pares = []
impares = []

for numeros in range(0, 20):
    inteiros.append(int(input('Informe 20 números inteiros: ')))

for i in inteiros:
    if i % 2 == 0:
        pares.append(i)
    if i % 2 == 1:
        impares.append(i)

print(f'os numeros informados foram: {inteiros}')
print(f'Os numeros pares encontrados foram: {pares}')
print(f'Os numeros ímpares encontrados foram: {impares}')
