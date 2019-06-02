from time import sleep as sl


def contagem(ini, fim, dist=1):
    print('-=' * 10)
    print(f'Contagem de {ini} ate {fim} de {dist} em {dist}')
    if fim > ini:
        for num in range(ini, fim+1, dist):
            print(f'{num}', end=' ')
        print('Fim!')
    else:
        for num in range(ini, fim-1, dist*-1):
            print(f'{num}', end=' ')
        print('Fim!')


contagem(1, 10)
contagem(10, 1)

print('Agora é sua vez')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)
