# Ex02. Faça um programa que peça 5 numeros e armazene-os em uma lista
lista_de_numeros = []

for i in range(1,6):
    numero = input(f'Digite o {i}º número da lista: ')
    lista_de_numeros.append(numero)

print(lista_de_numeros)