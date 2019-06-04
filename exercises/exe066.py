while True:
    n1 = int(input('Quer ver a tabuada de qual número: '))
    n2 = int(input('Tabuada até qual número? '))
    cont = 1
    while cont < (n2+1):
        print(f'{n1} X {cont} = {n1 * cont}')
        cont = cont + 1