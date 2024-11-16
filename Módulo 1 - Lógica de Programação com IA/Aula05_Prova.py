"""Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas.
Utilize um loop 'for' para iterar sobre os alunos e suas notas.
Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0.
Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
Ao final, exiba a média geral da turma."""

quant_alunos = int(input("Qual é a quantidade de alunos na disciplina? "))
alunos = []
notas1 = []
notas2 = []
notas3 = []
medias = []
resultados = []
media_turma = 0

for aluno in range(quant_alunos):
    aluno = input(f"Digite o nome do {aluno+1}° aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    media = (nota1 + nota2 + nota3) / 3

    alunos.append(aluno)
    notas1.append(nota1)
    notas2.append(nota2)
    notas3.append(nota3)
    medias.append(media)

    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    resultados.append(resultado)
    media_turma += media

for i in range(quant_alunos):
    print(f" Nome: {alunos[i]}, Nota 1: {notas1[i]}, Nota 2: {notas2[i]}, Nota 3: {notas3[i]}, Média: {medias[i]}, Resultado: {resultados[i]}")

print(f"Nota média geral da turma: {media_turma / quant_alunos}")