# Ex01. Faça um programa que peça: nome e 3 notas de um aluno, depois armazene no dicionário as seguintes informações:
# - nome
# - notas (lista)
# - media
# - situacao ('APROVADO' se maior que 6, se não, 'REPROVADO')

# Depois mostre as informações do aluno na tela.

aluno = {
    'nome': 'none',
    'notas': []
}

aluno['nome'] = input('Digite o nome do aluno: ')

for n in range(1,4):
    aluno = input(f'Digite a {n}º nota do aluno: ')

aluno['media'] = sum(aluno.get('notas'))
print(aluno)