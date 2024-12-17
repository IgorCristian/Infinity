# Projeto

# Você foi contratado para desenvolver um sistema de uma loja de doces que pretende realizar uma promoção onde um brinde será sorteado entre os clientes do dia. 
# O sorteio funcionará da seguinte forma:

# - O programa deve mostrar um Menu com 3 opções (Listar vendas, Registrar nova venda, Encerrar)

# - Ao registrar uma venda, o caixa da loja perguntará ao cliente sobre seu nome, telefone e endereço, 
# inscrevendo essas informações em uma aplicação que ficará executando durante todo o expediente da loja (ou seja: em processo de repetição).

# - A aplicação guardará todas as ocorrências de clientes informados (em uma lista de dicionários, ou lista de tuplas) até que o caixa seja encerrado.

# - No final do expediente, o caixa informará a opção de "encerrar", e a aplicação sorteará um dos clientes atendidos ao longo do dia.

# - A aplicação informará na tela todos os dados do cliente sorteado e se encerrará.


import assets.funcoes as fn

while True:
    print(' Loja do Povo '.center(30,'-'))
    print('[1] - Listar Vendas')
    print('[2] - Registrar Nova Venda')
    print('[3] - Sortear')
    print('[4] - Encerrar')
    print('-'*30)

    opcao = input('\033[32mDigite uma opção:\033[m ')

    if opcao == '1':
        fn.limpar(1)
        fn.listar_vendas()
    elif opcao == '2':
        fn.limpar(1)
        fn.registrar_nova_venda()
    elif opcao == '3':
        fn.limpar(1)
        fn.sortear()
    elif opcao == '4':
        encerrar = input('Tem certeza disso? Você perderá todas as informações. (S/N) ').lower()
        if encerrar == 's':
            print('\033[36mPrograma encerrado\033[m'.center(30,'-'))
            break
    else:
        print('\033[33mOpção Inválida. Digite Novamente.\033[m')
        fn.limpar(1)