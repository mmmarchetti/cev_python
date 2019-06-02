from random import randint as r
n = (r(1, 9), r(1, 9), r(1, 9), r(1,9), r(1, 9))
for c in n:
    print(c, end = ' ')
print('\nO maior valor é {}.' .format(max(n)))
print('O menor valor é {}.' .format(min(n)))