"""Atividade 01:
Contagem de 1 a 10:
Crie um programa que use um laço while
para contar de 1 a 10 e exibir cada número. """

"""numero = 1
while numero <= 10:
    print(numero)
    numero +=1"""

"""Atividade 02:
Soma de Números de 1 a 100:
Escreva um programa que use um laço while para
somar os números de 1 a 100 e exiba o resultado."""

"""numero = 1
soma = 0

while numero <= 100:
    soma += numero
    numero +=1
print(soma)"""

"""Atividade 08:
Média de Notas:
Desenvolva um programa que solicite as notas dos alunos até
que o usuário digite -1. Calcule e exiba a média das notas
inseridas."""

print("Calculo de notas.")
nota = float(input("Digite a sua primeira nota: "))
soma = 0
contador = 0.0

while nota != -1:
    soma += nota
    contador += 1
    nota = float(input("Digite sua outra nota: "))
print(f"Sua nota média é {soma / contador} pontos.")