# Projeto

# Você foi contratado para desenvolver um sistema de uma loja de doces que pretende realizar uma promoção onde um brinde será sorteado entre os clientes do dia. 
# O sorteio funcionará da seguinte forma:

# - O programa deve mostrar um Menu com 3 opções (Listar vendas, Registrar nova venda, Encerrar)

# - Ao registrar uma venda, o caixa da loja perguntará ao cliente sobre seu nome, telefone e endereço, 
# inscrevendo essas informações em uma aplicação que ficará executando durante todo o expediente da loja (ou seja: em processo de repetição).

# - A aplicação guardará todas as ocorrências de clientes informados (em uma lista de dicionários, ou lista de tuplas) até que o caixa seja encerrado.

# - No final do expediente, o caixa informará a opção de "encerrar", e a aplicação sorteará um dos clientes atendidos ao longo do dia.

# - A aplicação informará na tela todos os dados do cliente sorteado e se encerrará.

import random

vendas = {
    'nome': [],
    'telefone': [],
    'endereco': []
}


def registrar_nova_venda():
    vendas['nome'].append(input('Digite o nome do cliente: '))
    vendas['telefone'].append(input('Digite o telefone do cliente: '))
    vendas['endereco'].append(input('Digite o endereço do cliente: '))
    print('')
    return vendas
    

def listar_vendas():
    print(' Vendas de Hoje '.center(30,('-')))
    for venda in range(len(vendas['nome'])):
        print(f'Venda Nº {venda + 1}')
        print(f'Nome: {vendas['nome'][venda]}')
        print(f'Telefone: {vendas['telefone'][venda]}')
        print(f'Endereço: {vendas['endereco'][venda]}')
        print('*'*40)

def sortear():
    sorteio = random.randint(0, len(vendas['nome']) - 1)
    print('Cliente Sorteado'.center(30,'-'))
    print(vendas['nome'][sorteio])
    print(vendas['telefone'][sorteio])
    print(vendas['endereco'][sorteio])
    print('')

while True:
    print(' Loja do Povo '.center(30,'-'))
    print('[1] - Listar Vendas')
    print('[2] - Registrar Nova Venda')
    print('[3] - Sortear')
    print('[4] - Encerrar')
    print('-'*30)

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        listar_vendas()
    elif opcao == '2':
        registrar_nova_venda()
    elif opcao == '3':
        sortear()
    elif opcao == '4':
        encerrar = input('Tem certeza disso? Você perderá todas as informações. (S/N) ').lower()
        if encerrar == 's':
            print('Programa encerrado'.center(30,'-'))
            break
    else:
        print('Opção Inválida. Digite Novamente.')
