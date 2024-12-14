# [PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email.
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email.
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

# Criando dicionário
contato = {
    'nome': '',
    'telefone': '',
    'email': ''
}

# Solicita informações ao usuário
contato['nome'] = input('Insira o nome: ')
contato['telefone'] = input('Insira o número de telefone: ')
contato['email'] = input('Insira o endereço de email: ')

# Exibe informações registradas
print('Contato Registrado:')
print(f'Nome: {contato["nome"]}')
print(f'Telefone: {contato["telefone"]}')
print(f'Email: {contato["email"]}')