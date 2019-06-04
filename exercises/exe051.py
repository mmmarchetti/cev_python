print('-=' * 10)
print('10 Termos de uma PA')
print('-=' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dez = n + (10 - 1)
cont = n
for c in range (n, dez):
    print(f'{cont}', end = ' -> ')
    cont = cont + r
print('FIM')