#Como usar class.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print('Olá, meu nome é', self.nome, 'e eu tenho', self.idade, 'anos.')

pessoa1 = Pessoa('João', 30)
pessoa2 = Pessoa('Maria', 25)

print(pessoa1.nome)
print(pessoa2.idade)

pessoa1.apresentar()
pessoa2.apresentar()