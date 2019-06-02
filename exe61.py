print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = int(input('População PA: '))
while True:
    while x > 0:
        print(f'{n1}', end = ' ')
        print('->' if x > 1 else 'Fim', end = ' ')
        n1 = n1 + r
        x = x - 1
    if x == 0:
        sn = str(input('Quer continuar? [S/N]: '))
        if sn in 'Ss':
            x = int(input('Quantos termos mais? '))
        else:
            break
print('-FIM-')