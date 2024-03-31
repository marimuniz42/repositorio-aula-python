# Testando o conhecimento

name = input('Qual é o seu nome? ')

match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Grifinoria')
    case 'Draco':
        print('Sonserina')
    case _: # _ é igual a qualquer
        print('Quem')