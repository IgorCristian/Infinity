# Ex02. Faça um programa para pedir modelo, ano, preço fip e kilometragem de um carro (uso). Depois, calcule o preço final do carro a partir da kilometragem:

# - Km maior que 300_000, - 50%
# - Km maior que 200_000, - 35%
# - Km maior que 150_000, - 30%
# - Km maior que 100_000, - 20%
# - Outros Km             - 15%

carro = {}

carro["modelo"] = input("Digite o modelo do carro: ")
carro["ano"] = input("Digite o ano do carro: ")
carro["preco"]  = float(input("Digite o preço fip do carro: "))
carro["kilometragem"] = float(input("Digite a kilometragem do carro: "))

print(carro)

if carro["kilometragem"] > 300_000:
    valor = carro["preco"] - (0.5 * carro["preco"])
elif carro["kilometragem"] > 200_000:
    valor = carro["preco"] - (0.35 * carro["preco"])
elif carro["kilometragem"] > 150_000:
    valor = carro["preco"] - (0.30 * carro["preco"])
elif carro["kilometragem"] > 100_000:
    valor = carro["preco"] - (0.20 * carro["preco"])
else:
    valor = carro["preco"] - (0.15 * carro["preco"])

print(f'O valor do carro é R${valor}.')