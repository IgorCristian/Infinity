# Ex01. Faça um programa que peça 3 numeros e informe o maior e o menor.

lista_de_valores = []

for n in range(1,4):
    valores = int(input(f"Insira o {n}º valor: "))
    lista_de_valores.append(valores)

lista_ordenada = sorted(lista_de_valores)

print(lista_ordenada)
