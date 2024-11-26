# Ex02. Faça uma função "calcular_salario" que recebe um parametro "salario" e retorna o salario deduzido das seguintes taxas:

""" - IR: 8%
    - INSS: 5%
    - Sindicato: 3%"""

def calcular_salario(salario):
    deducao_ir = salario - (salario * 0.08)
    deducao_inss = deducao_ir - (deducao_ir * 0.05)
    deducao_sindicato = deducao_inss - (deducao_inss * 0.03)
    return deducao_sindicato

salario = calcular_salario(float(input('Digite qual é o seu salário para calcular as deduções de impostos: ')))

print(f'Você irá receber R${salario:.2f}')