from exercises.exe109.moeda import Calculo

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {Calculo(p, False).metade()}')
print(f'O dobro de {p} é {Calculo(p).dobro()}')
print(f'Aumentando 10% temos {Calculo(p).aumentar(10)}')
print(f'Diminuindo 13%, temos {Calculo(p).diminuir(13)}')
