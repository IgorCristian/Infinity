# Ex03. Você foi contratado por uma instituição de nutrição para ajuda-los em um sistema:

""" a. Faça uma função chamada "calcular_imc" que irá receber dois parametros ("peso" e "altura") e retornar o valor do imc

    b. Faça uma função chamada "classificar_"""

def calcular_imc(peso,altura):
    imc = peso / (altura * altura)
    return imc

def classificar(imc):
    classificacao = ""
    if imc < 18.5:
        classificacao = "Magreza"
    elif classificacao