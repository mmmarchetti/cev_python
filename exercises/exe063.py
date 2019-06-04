print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
t = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 0
print(f'{t1} -> {t2}', end = ' -> ')
while cont <= t:
    t3 = t1 + t2
    print(f'{t3}', end = ' ')
    print('->' if t > 1 else 'Fim.', end = ' ')
    t1 = t2
    t2 = t3
    cont = cont + 1