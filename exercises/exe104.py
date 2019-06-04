def leiaint(frase='Digite um número válido: '):

    while True:
        num = input(frase)
        if num not in '0123456789':
            print('ERRO! Digite um número inteiro válido!')

        else:
            break

    return num


n = leiaint('Digite um número válido: ')
print(f'Você digitou o número {n}')
