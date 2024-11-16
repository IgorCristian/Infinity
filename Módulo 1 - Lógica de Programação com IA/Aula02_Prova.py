print("Olá, você quer saber se o seu número é positivo, negativo ou zero? ")
numero = float(input("Para isso digite aqui o seu número: "))

if numero > 0:
    print(f"O número {numero} -9 é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número é igual a zero")