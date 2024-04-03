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