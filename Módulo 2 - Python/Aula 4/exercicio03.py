# Ex03. Faça uma função chamada "calcular_area_retangulo" que recebe dois parametros ("base" e "altura") e retorna a area do retangulo.

def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

base = float(input("Digite o tamanho da base em metros do retângulo: "))
altura = float(input("Digite o tamanho da altura em metros do retângulo: "))

calcular_area_retangulo(base, altura)

print(f'A área do retêngulo é {calcular_area_retangulo(base, altura)}m²')


