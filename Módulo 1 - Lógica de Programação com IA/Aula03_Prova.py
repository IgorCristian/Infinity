"""[LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação.
O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.
Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas.
Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso."""

print("Bem vindo ao jogo de adivinhação: ")
print("Você terá 3 tentativas para adivinhar qual é o número correto entre 1 a 10.")

numero = 7
tentativa = 1
chute = int(input("Faça sua primeira tentativa: "))

while tentativa <= 3:
    tentativa += 1
    if chute == 7:
        print("Parabéns você acertou!!!")
        break
    elif tentativa == 2:
        chute = int(input(f"Você errou, mas vamos lá você ainda têm mais {tentativa} tentativas: "))
    elif tentativa == 3:
        chute = int(input(f"Número errado, mas não desanime, você têm mais uma chance: "))
    else:
        print("Uhmm errou de novo, e infelizmente suas chances acabaram, boa sorte na próxima.")
print("Jogo Encerrado!")