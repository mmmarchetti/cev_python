nasc = int(input('Digite o ano de seu nascimento: '))
idade = (2018 - nasc)
print(f'Você tem {idade} anos em 2018')
alist = 18 - idade
if alist < 0:
    print(f'Você devia ter se alistado a {(alist)*-1} anos.')
elif alist == 0:
    print('Este ano você deve se alistar.')
else:
    print(f'Você ainda tem {alist} anos para se alistar.')