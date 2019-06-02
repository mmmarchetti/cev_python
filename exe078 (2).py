num = []
pos = 0
for c in range(0, 4):
    num.append(input('Digite um número na posição {}: ' .format(pos)))
    pos = pos + 1
print('Os valores digitados foram: {}' .format(num))
cont = 0
print('O menor valor digitidado foi o {} e apareceu na posição:' .format(min(num))), end = ' ')
for c in num:
    if c in min(num):
        print('{}... ' .format(cont), end = ' ')
    cont = cont + 1
print('')
con = 0
print('O maior valor digitado foi o {} e apareceu na posição:' .format(max(num))), end = ' ')
for n in num:
    if n in max(num):
        print('{}... ' .format(con), end = ' ')
    con = con + 1
print('')