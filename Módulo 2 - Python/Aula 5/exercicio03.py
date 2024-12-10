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

# Cria a lista e adiciona o primeiro nome:
nomes = [(input('Adicione um nome na lista: '))]


# Loop para adição de nomes na lista
while True:
    continua = input("Você deseja adicionar mais um nome na lista? (S/N)").lower()
    if continua == "s":
        nomes.append(input("Digite mais um nome: "))
    else:
        break

# Chama função para listar nomes
listar_nomes(nomes)