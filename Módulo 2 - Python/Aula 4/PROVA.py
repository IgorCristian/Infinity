# [PYIA-A04] Crie uma função chamada media que receberá três números como argumentos.
# Esta função deve calcular a média aritmética desses três números.
# Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

def media (n1: float, n2: float, n3: float) -> float:
    """Função recebe três valores e retorna 
    a média entre eles

    Args:
        n1 (float): primeiro valor
        n2 (float): segundo valor
        n2 (float): terceiro valor

    Returns:
        float: média aritmética calculada
    """
    media = (n1 + n2 + n3) / 3
    return round(media ,2)

n1 = 6
n2 = 4
n3 = 15

print(f'A média aritmética calculada é: {media(n1, n2, n3)}')