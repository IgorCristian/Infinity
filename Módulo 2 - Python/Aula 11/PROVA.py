#[PYIA-A11] Crie três classes separadas e independentes: Animal, Cachorro e Gato.
#Cada classe deve ter um método chamado falar (), que imprime uma mensagem específica na tela:
#- A classe Animal deve imprimir: "Este animal faz um som genérico."
#- A classe Cachorro deve imprimir: "O cachorro está latindo."
#- A classe Gato deve imprimir: "O gato está miando."

#Regras:
#- As classes não devem se relacionar entre si.
#- Cada classe deve ser criada de forma independente.
#- No final, crie um objeto para cada uma das classes e chame o método falar () de cada objeto.


# Classe Animal
class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")

# Classe Cachorro
class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")

# Classe Gato
class Gato:
    def falar(self):
        print("O gato está miando.")

# Criando objetos de cada classe
animal = Animal()
cachorro = Cachorro()
gato = Gato()

# Chamando o método falar() de cada objeto
animal.falar()
cachorro.falar()
gato.falar()
