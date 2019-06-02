lista = []
continua = 'S'
while continua in 'S':
    dig = int(input('Digite um valor: '))
    if dig in lista:
        print('Valor aduplicado! ...')
        continua = str(input('Quer continuar? [S/N]: ')).upper()
        while continua not in 'SN':
            continua = str(input('Por favor digite S ou N: ')).upper()
    else:
        lista.append(dig)
        print('Valor adicionado com sucesso...')
        continua = str(input('Quer continuar? [S/N]: ')).upper()
        while continua not in 'SN':
            continua = str(input('Por favor digite S ou N: ')).upper()
print('-=' * 20)
print('Você adicionou os valores {}' .format(lista))