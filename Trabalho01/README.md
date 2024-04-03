# Trabalho 01

Escreva um programa em Python que classifique as pessoas em categorias com base em suas idades. O programa deve solicitar ao usuário que insira sua idade e, em seguida, imprimir a categoria apropriada de acordo com as seguintes regras:

- Se a idade for menor que 12 anos, a pessoa está na categoria "Criança".
- Se a idade for pelo menos 12 anos, mas menor que 18 anos, a pessoa está na categoria "Adolescente".
- Se a idade for pelo menos 18 anos, mas menos que 60 anos, a pessoa está na categoria "Adulto".
- Se a idade for 60 anos ou mais, a pessoa está na categoria "Idoso".

O programa deve incluir:

- Solicitação da idade do usuário.
- Uso de condicionais para determinar a categoria.
- Impressão da categoria apropriada.

Código base:

```py
idade = int(input('Digite sua idade: '))
```

## Resposta:
```py
#Trabalho da aula 01

#Recebe a idade do usuário
while True:
    try:
        idade = int(input('Digite sua idade: '))
        break
    except ValueError: #Caso o usuário digite uma idade inválida, pede para o usuário por um número inteiro
        print("Digite um número inteiro.")

#Faz a classificação
if idade < 12:
    categoria = 'Criança'
elif idade < 18:
    categoria = 'Adolescente'
elif idade < 60:
    categoria = 'Adulto'
else:
    categoria = 'Idoso'

#Comunica qual a a classificação
print(f'Caro usuário sua categoria é {categoria}.')
```