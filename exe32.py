ano = int(input('Digite um ano: '))
if (ano % 4) != 0 and (ano % 400) != 0:
    print('O ano {} não é bissexto.' .format(ano))
while (ano % 4) == 0 or (ano % 400) ==0:
    if (ano % 100) == 0:
        print('O ano {} não é bissexto.' .format(ano))
        break
    else:
        print('O ano {} é bissexto' .format(ano))
        break
print('-fim-')