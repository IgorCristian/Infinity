"""1. Peça ao usuário para inserir um número inteiro e conte quantos dígitos ele possui. Imprima o total. """

numero = input("Digite um número inteiro para descobrir a quantidade de dígitos que ele possui. ")
digitos = 0

#Como a váriável "numero" recebe um valor como string, foi utilizado a estrutura de repetição for para contar a quantidade de caracteres e mostrar quantos dígitos o número possui.
for i in numero:
    digitos += 1
print(f"Esse número possui {digitos} digitos.")