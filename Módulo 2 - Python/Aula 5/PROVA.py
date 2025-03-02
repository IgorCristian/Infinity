# [PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos.
# Esta função deve comparar os três números e identificar qual deles é o maior.
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois.
# A função deve então retornar o maior número encontrado.

def maior_numero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else: 
        return n3

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f'O maior número é: {maior_numero(n1,n2,n3)}')