# Ex02. Crie um dicionário que armazene as idades de 5 pessoas (Já preenchido),usando o nome como chave e a idade como valor. Então.

# a. Adicione uma nova pessoa ao dicionário com seu respectivo nome e idade e exiba o dicionário atualizado.

# b. Utilize um for para adicionar 3 novas pessoas ao invés de uma


pessoas = {
    'nome': ['Maria', 'José', 'Marta', 'Ana', 'Carlos'],
    'idade': [50, 60, 31, 15, 8]
}

pessoas['nome'].append(input('Insira o nome da próxima pessoa: '))
pessoas['idade'].append(int(input('Agora insira a idade dessa nova pessoa adicionada: ')))

print(pessoas)

for i in range(4,7):
    pessoas['nome'].append(input(f'Insira o nome da {i}º pessoa: '))
    pessoas['idade'].append(input(f'Agora insira a idade da {i}º pessoa: '))

print('<----Pessoas Cadastradas---->')
for i in range(len(pessoas['nome'])):
    print(f'Nome: {pessoas['nome'][i]}, Idade: {pessoas['idade'][i]} anos.')