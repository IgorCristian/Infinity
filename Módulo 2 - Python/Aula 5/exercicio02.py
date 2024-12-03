# Ex02. Faça uma função chamada "verificar_par" que recebe um numero e retorna um booleano (True se for par, False se for impar)

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um número inteiro para verificar se ele é par ou ímpar: '))

print(f'{verificar_par(numero)}')
