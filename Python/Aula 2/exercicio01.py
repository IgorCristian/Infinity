# Ex01. Faça um programa que peça: nome e 3 notas de um aluno, depois armazene no dicionário as seguintes informações:
# - nome
# - notas (lista)
# - media
# - situacao ('APROVADO' se maior que 6, se não, 'REPROVADO')

# Depois mostre as informações do aluno na tela.
notas = []

aluno = {
    'nome': 'none',
    'notas': notas,
    'media': 'none',
    'situacao': 'none',
}

aluno['nome'] = input('Digite o nome do aluno: ')

for n in range(1,4):
    notas = input(f'Digite a {n}º nota do aluno: ')

print(aluno)