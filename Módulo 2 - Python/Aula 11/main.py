print(type('ola'))

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def chorar(self):
            print(f'Bebê {self.nome} está chorando.')

    def aniversario(self):
            self.idade += 1
            print(f'Parabéns, {self.nome} agora têm {self.idade} anos.')

pessoa1 = Pessoa('Lucas',1)


pessoa1.chorar()

print(type(Pessoa))

