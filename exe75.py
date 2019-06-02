#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor: '))
#n3 = int(input('Digite mais outro: '))
#n4 = int(input('Digite o último: '))
#nt = (n1, n2, n3, n4)
#par = 0
#print(f'O valor 9 apareceu {nt.count(9)} vezes.')
#if nt.count(3) > 0:
#    print(f'O valor 3 apareceu na posição {nt.index(3)+1}.')
#else:
#    print('O valor 3 não apareceu em nenhuma posição.')
#for c in nt:
#    if c % 2 == 0:
#        par = par + 1
#if par > 0:
#    print('Os números pares são: ', end = ' ')
#else:
#    print('Não há números pares.')
#for c in nt:
#    if c % 2 == 0:
#        print(f'{c}', end = ' ')
#print('-='*20, 'Com listas', '-=' * 20)
par = 0
n = []
qn = int(input('De quantos números precisa? '))
for c in range (0, qn):
    n.append(int(input('Digite um valor: ')))
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if n.count(3) > 0:
    print(f'O valor 3 apareceu na posição {n.index(3)+1}.')
else: 
    print('O valor 3 não apareceu.')
for cont in n:
    if cont % 2 == 0:
        par = par + 1
if par > 0:
    print('Os números pares digitados foram: ', end = ' ')
else:
    print('Não há números pares na lista.')
for cont in n:
    if cont % 2 == 0:
        print(f'{cont}', end = ' ')