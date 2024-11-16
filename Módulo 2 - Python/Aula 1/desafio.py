#Desafio: Faça um programa que peça 2 numeros, depois armazene em uma lista "primos" todos os numeros primos entre os numeros informados (eles inclusos.)

# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita ao usuário dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Garante que num1 seja o menor e num2 o maior
inicio = min(num1, num2)
fim = max(num1, num2)

# Lista para armazenar os números primos
primos = []

# Loop para verificar cada número no intervalo
for numero in range(inicio, fim + 1):
    if eh_primo(numero):
        primos.append(numero)

# Exibe a lista de números primos
print("Números primos entre", num1, "e", num2, "são:", primos)