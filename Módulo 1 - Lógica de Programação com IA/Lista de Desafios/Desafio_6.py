"""6. Peça ao usuário para inserir uma lista de números e retorne a soma total. """
lista_numeros = []
soma = 0

while True:
    numero = input("Digite um número ou digite (fim) para parar:")
    if numero == "fim":
        break
    else:
        lista_numeros.append(float(numero))
for n in lista_numeros:
    soma += n
print(f"A soma dos números {lista_numeros} é {soma}")