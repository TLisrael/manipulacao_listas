# Faça um Programa que peça as quatro notas de 10 alunos,
# Calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

medias = []
media_sete = 0

for aluno in range(10):
    soma_notas = 0
    for nota in range(4):
        c = eval(input(f'Digite a {nota+1}º do {aluno+1}º aluno: '))
        soma_notas += c
    medias.append(soma_notas / 4)
    if medias[aluno] >= 7:
        media_sete += 1

print(f'Media dos alunos {medias}')
print(f'Alunos com medias sete {media_sete}')