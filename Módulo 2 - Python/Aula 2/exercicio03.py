#Ex03. Dado o dicionário abaixo, remova o item com a chave "laranja" (utilizando a função pop()) e exiba o dicionário atualizado.

"""python
estoque = {"banana": 10, "laranja": 5, "uva": 8}
"""

estoque = {
    'banana': 10, 
    'laranja': 5,
    'uva': 8,
}

print(estoque)

estoque.pop('laranja')

print(estoque)
