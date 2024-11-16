""" Crie um programa em Python que simule um sistema de login.
O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos.
Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam.
Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.

Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes."""

usuario_cadastrado = "Jubileu"
senha_cadastrada = "123456"
tentativa = 3

while tentativa > 0:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print(f"Olá {usuario}, seja bem vindo!")
        break
    else:
        tentativa -= 1
        if tentativa > 0:
            print(f"Usuário ou senha incorreta, você têm mais {tentativa} tentativa(s). ")
        else:
            for i in range(3):
                print("Acesso Bloqueado.")