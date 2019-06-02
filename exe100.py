def sorteio():
    from random import randint as rd
    cont = rd(1, 9)
    soma = 0
    lista = []
    print(f'Sorteando {cont} valores de lista: ')
    for num in range(0, cont):
        sorteio = rd(1, 9)
        print(f'{sorteio}', end=' ')
        lista.append(sorteio)
    print('Pronto!')
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteio()
