def fatorial(num):
    fat = 1
    for cont in range(1, num+1):
        fat *= cont
    return fat


def dobro(num):
    return num * 2


def triplo(num):
    return num * 3


numero = int(input('Digite um número: '))
fator = fatorial(numero)

print(f'O fatorial de {numero} é igual a {fator}')







