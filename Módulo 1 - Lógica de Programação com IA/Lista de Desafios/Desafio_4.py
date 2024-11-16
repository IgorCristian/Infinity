"""4. Peça ao usuário para inserir dois números e imprima a soma deles. Depois, pergunte se ele deseja somar mais um número e repita o processo, exibindo a nova soma. """
#Usuário define o cálculo inicial
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
soma = numero1 + numero2

#Mostra o resultado inicial
print(f"A soma de {numero1} + {numero2} é = {soma}")

#Inicia a análise do usuário para prosseguir como verdadeiro
usuario = 1

while usuario == True:
    usuario = int(input("Você deseja somar mais um número? Se sim digite (1) se não digite (0): "))
    if usuario == 1:
        soma += int(input("Digite o número a ser somado: "))
        print(soma)
    elif usuario == 0:
        print(f"Ok, conta encerrada, o resultado final é {soma}.")
    else:
        print("ERRO, Comando não encontrado!")
        