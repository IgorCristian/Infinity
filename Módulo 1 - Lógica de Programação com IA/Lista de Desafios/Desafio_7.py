"""7. Leia uma string e conte quantas vogais existem nela. """

def contar_vogais(texto):
  """Conta o número de vogais em uma string.

  Args:
    texto: A string a ser analisada.

  Returns:
    O número de vogais na string.
  """

  vogais = "aeiouAEIOU"
  contador = 0
  for letra in texto:
    if letra in vogais:
      contador += 1
  return contador

# Solicita a entrada do usuário
texto = input("Digite uma frase ou palavra: ")

# Chama a função e imprime o resultado
num_vogais = contar_vogais(texto)
print(f"A frase '{texto}' possui {num_vogais} vogais.")