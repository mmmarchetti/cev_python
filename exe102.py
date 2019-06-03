def fatorial(num, show=True):
    fat = num
    for cont in range(num, 0, -1):
        fat *= cont
        if show:
            print(f'{cont}', end=' ')
            if cont != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    print(fat)


fatorial(4)
