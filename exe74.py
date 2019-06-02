from random import randint as r
n1 = r(1, 9)
n2 = r(1, 9)
n3 = r(1, 9)
n4 = r(1, 9)
n5 = r(1, 9)
nt = (n1, n2, n3, n4, n5)
print(f'Os números sorteados foram: ', end = ' ')
for n in nt:
    print(f'{n}', end = ' ')
print(f'\nO maior número sorteado foi {max(nt)}.')
print(f'O menor número sorteado foi {min(nt)}.')