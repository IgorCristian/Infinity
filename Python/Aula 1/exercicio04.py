# Ex04. Faça um programa que peça 6 numeros, e armazene-os em duas listas: "pares" e "impares".
# Depois mostre-as na tela

numeros = []
pares = []
impares = []

for i in range(1,7):
    numero = int(input(f'Digite o {i}º número da lista: '))
    numeros.append(numero)