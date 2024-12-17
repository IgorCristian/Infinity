import random as rd
import time
import os


vendas = {
    'nome': [],
    'telefone': [],
    'endereco': []
}

def limpar(tempo):
    time.sleep(tempo)
    os.system("clear")# PARA WINDOWS USE NO LUGAR DE CLEAR O "cls"

def registrar_nova_venda():
    print('Registrando Venda'.center(30,'-'))
    vendas['nome'].append(input('Digite o nome do cliente: '))
    vendas['telefone'].append(input('Digite o telefone do cliente: '))
    vendas['endereco'].append(input('Digite o endereço do cliente: '))
    print('')
    print("\033[32mVenda realizada com sucesso\033[m")
    limpar(2)
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
    sorteio = rd.randint(0, len(vendas['nome']) - 1)
    print('Cliente Sorteado'.center(30,'-'))
    print(vendas['nome'][sorteio])
    print(vendas['telefone'][sorteio])
    print(vendas['endereco'][sorteio])
    print('')