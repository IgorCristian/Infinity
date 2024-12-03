# Ex04. Você foi contratado por uma instituição de nutrição para ajuda-los em um sistema:

"""a. Faça uma função chamada "calcular_imc" que irá receber dois parametros ("peso" e "altura") e retornar o valor do imc.
    b. Faça uma função chamada "classificar_imc" que recebe o IMC e retorna uma string com a situação da pessoa baseado na tabela IMC:

    - "ABAIXO_DO_PESO"  -> Imc <= 18.5
    - "PESO_IDEAL"      -> Imc <= 25
    - "SOBREPESO"       -> Imc <= 30
    - "OBESIDADE_I"     -> imc <= 35
    - "OBESIDADE_II"    -> imc <= 40
    - "OBESIDADE_III"   -> imc > 40"""

def calcular_imc(peso: float, altura: float) -> float:
    imc = peso / (altura * altura)
    print(f'O seu imc é: {round(imc, 2)}')
    return imc
    

def classificar(imc: float) -> str:
    if imc <= 18.5:
        classificacao = "ABAIXO_DO_PESO"
    elif imc <= 25:
        classificacao = "PESO_IDEAL"
    elif imc <= 30:
        classificacao = "SOBREPESO"
    elif imc <= 35:
        classificacao = "OBESIDADE_I"
    elif imc <= 40:
        classificacao = "OBESIDADE_II"
    else:
        classificacao = "OBESIDADE_III"
    print(f'Situação: {classificacao}')

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = calcular_imc(peso,altura)
classificar(imc)

