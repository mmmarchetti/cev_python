n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa')
    op = int(input('Qual opção desejada? '))
    if op == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
        break
    elif op == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
        break
    elif op == 3:
        print(f'O maior valor entre {n1} e {n2} é {max(n1, n2)}.')
        break
    elif op == 4:
        print('Selecione uma nova opção.')
    elif op == 5:
        sair = str(input('Tem certeza que deseja sair? [S/N]'))
        if sair in 'Nn':
            print('Selecione uma nova opção.')
        elif sair in 'Ss':
            print('Saindo.')
            break
        else:
            print('Opção inválida')
print('-Fim-')