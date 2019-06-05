from exercises.exe112.moeda import Calculo


def leia_dinheiro(frase='Digite o preço: '):

    while True:
        num = input(frase)
        if num[:1] not in '0123456789':
            print(f'ERRO! {num} não é um número válido!')

        else:
            try:
                num = int(num)
            except ValueError:
                num = float(num.replace(',', '.'))
                break

    return num


p = leia_dinheiro('Digite o valor: R$')
Calculo(p, 10, 25).conta()
