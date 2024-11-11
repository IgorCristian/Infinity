# Ex04. Faça um programa que peça 6 numeros, e armazene-os em duas listas: "pares" e "impares".
# Depois mostre-as na tela

pares = []
impares = []

for i in range(1,7):
    numero = int(input(f'Digite o {i}º número da lista: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Estes são os números pares: {pares}")
print(f"Estes são os números ímpares: {impares}")
