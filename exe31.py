val = int(input('Digite a distância da viagem em km: '))
if val >= 200:
    print('O valor da viagem será de: R${}' .format(val * 0.85))
else:
    print('O valor da viagem será de: R${}' .format(val * 1.00))
print('-fim-')
    