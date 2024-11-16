"""3. Peça ao usuário para inserir uma palavra e imprima a palavra ao contrário. """

palavra = input("Insira uma palavra: ")
palavra_invertida = ""

for l in palavra[::-1]:
    palavra_invertida += l
print(palavra_invertida)