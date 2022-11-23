# Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(0, 10):
    letras.append(input('Informe um caracter: ').upper())

valor_consoante = 0
consoantes = []
for i in range(0, 10):
    if letras[i] not in vogais:
        consoantes.append(letras[i])
        valor_consoante += 1
print(f'Numero de consoantes {valor_consoante}')
print(consoantes)