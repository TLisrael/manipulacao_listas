# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [9, 7.8, 6.6, 9.8]
media = 0
for i in notas:
    media += i / 4
    if media >= 6:
        resultado = f'Aprovado! Media = {media}'
    else:
        resultado = f'Reprovado! Media = {media}'
print(resultado)
