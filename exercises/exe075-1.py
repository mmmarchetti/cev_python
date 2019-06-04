n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
num = (n1, n2, n3, n4)
print('O valor 9 apareceu {} vezes.' .format(num.count(9)))
if 3 in num:
    print('O valor 3 foi digitado na {}ª vez.' .format(num.index(3)+1))
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram:', end = ' ')
for c in num:
    if c % 2 == 0:
        print(c, end = ' ')