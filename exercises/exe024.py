nome = input('Digite o seu nome: ')
print(f'A primeira letra do seu nome Ã© {nome[0]}')
if nome.isalpha() is True:
    print('Seu nome não tem números!')
else:
    print('Seu nome tem números, que diferente!')


