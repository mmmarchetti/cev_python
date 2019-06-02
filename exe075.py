num = []
for c in range(0, 4):
    num.append(int(input('Digite um número: ')))
if 9 in num:
    print('O número 9 apareceu {} vez(es).' .format(num.count(9)))
else:
    print('Não foi digitado o número 9.')
par = 0
for n in num:
    if n % 2 == 0:
        par = par + 1
if par != 0:
    print('Os números pares digitados foram:', end = ' ')
else:
    print('Não houve número par digitado.')
for p in num:
    if p % 2 == 0:
        print(p, end = ' ')
if 3 in num:
    print('\nO número 3 foi digitado na {}ª vez.' .format(num.index(3)+1))
else:
    print('\nO número 3 não foi digitado.')