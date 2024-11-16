"""5.  Escreva uma função que gere os primeiros X números da sequência de Fibonacci onde X é um número informado pelo usuário."""

def fibonacci(x):
  """Gera os primeiros X números da sequência de Fibonacci.

  Args:
    x: O número de elementos da sequência a ser gerada.

  Returns:
    Uma lista contendo os primeiros X números da sequência de Fibonacci.
  """

  fibonacci_sequence = [0, 1]  # Inicializa a sequência com os dois primeiros números
  if x <= 2:
      return fibonacci_sequence[:x]  # Retorna os primeiros x elementos se x for menor ou igual a 2

  for i in range(2, x):
      next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
      fibonacci_sequence.append(next_number)

  return fibonacci_sequence 


# Obtém o número de elementos da sequência do usuário
n = int(input("Digite o número de elementos da sequência de Fibonacci: "))

# Chama a função e imprime o resultado
resultado = fibonacci(n)
print(resultado)