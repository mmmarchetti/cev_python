nome = input('Digite o seu nome: ')
print(f'A primeira letra do seu nome é {nome[0]}')
if nome.isalpha() is True:
    print('Seu nome n�o tem n�meros!')
else:
    print('Seu nome tem n�meros, que diferente!')


