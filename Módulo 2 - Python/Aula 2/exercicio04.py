#Ex04. Dado o dicionário abaixo, que representa o salário de diferentes cargos em uma empresa, some os salários de todos os cargos e exiba o total.

"""python
salarios = {
    "gerente": 5000, 
    "analista": 4000, 
    "desenvolvedor": 3500, 
    "estagiário": 1500
}
"""

salarios = {
    "gerente": 5000, 
    "analista": 4000, 
    "desenvolvedor": 3500, 
    "estagiário": 1500
}

lista_de_salarios = []

for valor in salarios:
    lista_de_salarios.append(salarios[valor])

print(lista_de_salarios)
print(f'A soma dos salários é R${sum(lista_de_salarios)}.')