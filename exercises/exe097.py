def escreva(palavra):
    for i in palavra:
        print('~', end='')
    print(f'\n{palavra}')
    for i in palavra:
        print('~', end='')


escrita = str(input('Digite a palavra: '))
escreva(escrita)
