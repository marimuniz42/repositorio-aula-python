# Aula 2 - CS50

## Exemplo 1:

Exemplo que ensina como usar while.

```py
i = 3

while i != 0:
    print('meow')
    i = i - 1
```

## Exemplo 2:

Outro exemplo que ensina como usar while.

```py
i = 3

while i != 0:
    print('meow')
    i = i - 1
```

## Exemplo 3:

Mais um exemplo que ensina como usar while.

```py
i = 3

while i != 0:
    print('meow')
    i = i - 1
```

## Exemplo 4:

Exemplo que ensina como usar for.

```py
for i in [0,1,2]:
    print('meow')
```

## Exemplo 5:

Exemplo que ensina como usar class.

```py
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
```