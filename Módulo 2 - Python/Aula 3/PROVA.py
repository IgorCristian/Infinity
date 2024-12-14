# [PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço.
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave.
# Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

# Cria dicionário e variável de soma do carrinho de compras
produtos = {}
soma = 0

# Solicita informações da compra e adiciona valor no carrinho
for i in range(4):
    produto = input('Digite o nome do produto: ')
    produtos[produto] = float(input('Digite o valor do produto: ').replace(',',('.')))
    soma += produtos[produto]

print(produtos)

# Exibe o valor da compra
print(f'Valor total da compra: R${soma}')