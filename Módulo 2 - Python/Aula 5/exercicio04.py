# Ex04. Faça uma função chamada "cadastrar_pessoa" que não conterá parametros, e irá retornar um dicionário com as chaves "nome", "idade" e "profissao".
# Os dados serão solicitados através de um input dentro da função.

def cadastrar_pessoa():
    
   pessoa = {}
   pessoa["nome"] = input("Digite o nome: ")
   pessoa["idade"] = input("Digite a idade: ")
   pessoa["profissao"] = input("Digite a profissão: ")
   return pessoa

print(f"Usuário Cadastrado: {cadastrar_pessoa()}.")