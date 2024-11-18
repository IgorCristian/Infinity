# Ex01. Faça um programa que peça: nome e 3 notas de um aluno, depois armazene no dicionário as seguintes informações:
# - nome
# - notas (lista)
# - media
# - situacao ('APROVADO' se maior que 6, se não, 'REPROVADO')

# Depois mostre as informações do aluno na tela.

aluno = {
    'nome': 'none',
    'notas': [],
}

aluno['nome'] = input('Digite o nome do aluno: ')

# Solicita as notas do aluno e guarda na lista de "notas" dentro do dicionário "aluno"
for n in range(1,4):
    nota = float(input(f'Digite a {n}º nota do aluno: '))
    aluno['notas'].append(nota)

# Calcula a "media" das notas
aluno['media'] = sum(aluno.get('notas')) / len(aluno.get('notas'))

#  Condição que informa a situação do aluno e printa na tela.
if aluno['media'] > 6:
    print(f'O aluno {aluno['nome']} foi APROVADO com uma média de {aluno['media']:.2f} pontos.')
else:
    print(f'O aluno {aluno['nome']} foi REPROVADO com uma média de {aluno['media']:.2f} pontos.')
