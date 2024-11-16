"""Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário.
O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares.
Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso."""

inicio = int(input("Insira um número inteiro para determinar o inicio do intervalo: "))
fim = int(input("Insira mais um número inteiro para determinar o fim do intervalo: "))
soma = 0
for n in range(inicio, fim+1):
    if n % 2 == 0:
        soma += n
        print(n)
if soma > 0:
     print (f"A soma dos números pares nesse intervalo é: {soma}")
else:
     print("Não há números pares nesse intervalo.")