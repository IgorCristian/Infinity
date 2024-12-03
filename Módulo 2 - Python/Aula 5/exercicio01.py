# Ex01. Faça uma função "calcular_media" que recebe 3 numeros e retorna a média desses numeros.

def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

print(f'A média dos números é: {calcular_media(n1,n2,n3)}')