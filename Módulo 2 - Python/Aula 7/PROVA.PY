# [PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados.
# Cada dado deve gerar um número aleatório entre 1 e 6.
# A função deve somar os resultados desses dois lançamentos e retornar o valor total.

from random import randrange

def lancar_dados():
    dado_1 = int(randrange(1,7))
    dado_2 = int(randrange(1,7))
    total = dado_1 + dado_2

    print(f'{dado_1} + {dado_2}')

    return total

resultado = lancar_dados()
print(f'O valor total é: {resultado}')
