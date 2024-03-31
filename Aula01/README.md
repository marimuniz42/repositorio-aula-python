# Aula 1 - CS50

## Exemplo 1:

Exemplo que ensina como usar input e f(format string).

```py
nome = input('Qual o seu nome? ')
#f é format string deixa o código de uma maneira mais prática e melhora a formatação.
print(f'Olá, {nome}')
```

## Exemplo 2:

Exemplo que ensina como calcular.

```py
x = int(input('O quanto é x?: '))
y = int(input('Quanto é y?: '))

print(x + y)
```

## Exemplo 3:

Exemplo que ensina como fazer função.

```py
def main():
    name = input('Qal o seu nome? ')
    hello(name)

def hello(para):
    print('Ola,', para)

main()
```

## Exemplo 4:

Exemplo que ensina como usar condições.

```py
x = int(input('O quanto é x?: '))
y = int(input('Quanto é y?: '))

if x < y:
    print('x é menor que y')
elif x > y:
    print('x é maior que y')
else:
    print('x é igual a y')
```

## Exemplo 5:

Exemplo que ensina como usar match.

```py
name = input('Qual é o seu nome? ')

match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Grifinoria')
    case 'Draco':
        print('Sonserina')
    case _: # _ é igual a qualquer
        print('Quem')
```