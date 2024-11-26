# Ex03. Faça um programa que peça uma quantidade indefinida de numeros e adicione-os em uma lista, 
# a cada valor inserido pergunte se o usuário deseja continuar, depois mostre o maior e o menor numero digitado.

# ENTRADA
numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    resp = input('Deseja Continuar [S/N]? -> ')
    if resp.upper() == 'N':
        break

# PROCESSAMETNO
maior = menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero


# SAÍDA
print(f'Números Digitados: {numeros}')
print(f'Número Maior: {maior}')
print(f'Números Menor: {menor}')
print('Fim do Programa.')