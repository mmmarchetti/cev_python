def analise(* num):
    soma = 0
    cont = 0
    maior = 0
    for i in num:
        print(f'{i}', end=' ')
        soma += i
        cont += 1
        if i > maior:
            maior = i
    print(f'\nForam informados {cont} valores.')
    print(f'A soma dos valores é igual a {soma}')
    print(f'O maior numero é {maior}')


analise(1, 2, 3)

analise(4, 5, 7, 9)
