# Ex03. Faça um programa que peça o nome e 3 notas de um aluno, e armazene as notas em uma lista "notas", depois calcule a média do aluno utilizando as funções "sum" e "len".

aluno = input('Digite o nome do aluno: ')
notas = []

for i in range(1,4):
    nota = float(input(f'Digite a {i}º nota do aluno: '))
    notas.append(nota)

print(f'A nota média do aluno {aluno} foi: {sum(notas) / len(notas)} pontos.')