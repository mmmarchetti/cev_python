n = int(input('Digite um número para calcular o fatorial: '))
calc = 1
print(f'Calculando {n}! = ', end = '')
for c in range (n, 0, -1):
    print(f'{c} X ', end = ' ')
    calc = calc * c
print(f'=  {calc}')
print('-='*5, 'Segunda maneira', '-='*5)

cal = 1
print(f'Calculando {n}! = ', end = '')
while n > 0:
    print(f'{n} ', end = '')
    print('x ' if n > 1 else ' = ', end = '')
    cal = cal * n
    n = n - 1
print(f'{cal}')    