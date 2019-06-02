num = int(input('Digite um número inteiro: '))
conv = ('Binário', 'Octal', 'Hexadecimal')
print('Escolha uma base para conversão: ')
print('[1] Para Binário \n[2] Para Octal \n[3] Para Hexadecimal')
while True:
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        print(f'O número {num} convertido para Binário é {bin(num)}' )
        break
    elif escolha == 2:
        print(f'O número {num} convertido para Octal é {oct(num)}.')
        break
    elif escolha == 3:
        print(f'O número {num} convertido para Hexadecimal é {hex(num)}.')
        break
    else:
        print('Opção inválida')