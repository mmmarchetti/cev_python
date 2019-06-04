numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze')
digitado = int(input('Digite um número entre 1 e 15: '))
cont = 1
for c in numeros:
    if cont == digitado:
        num = c
    cont = cont + 1
print('O número {} por extenso é: {}.' . format(digitado, num))