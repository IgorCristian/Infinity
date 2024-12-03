# Ex03. Faça uma função "listar_nomes" que recebe uma lista de nomes e mostra todos os nomes no formato abaixo:
# Dica: Utilize um For

# Entrada: ["Marcos", "Gabriel", "Lidia"]
# """
# Nomes:
# - Marcos
# - Gabriel
# - Lidia
# """

def listar_nomes(nomes):
    print('Nomes: ')
    for nome in nomes:
        print(f'- {nome}')

nomes = ["Marcos", "Gabriel", "Lidia"]

listar_nomes(nomes)