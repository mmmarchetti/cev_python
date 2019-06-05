from exercises.exe107.moeda import Calculo
from exercises.exe108.moeda_ptbr import formata_moeda as fm

p = float(input('Digite o preço: R$'))
print(f'A metade de {fm(p)} é {fm(Calculo(p).metade())}')
print(f'O dobro de {fm(p)} é {fm(Calculo(p).dobro())}')
print(f'Aumentando 10% temos {fm(Calculo(p).aumentar(10))}')
print(f'Diminuindo 13%, temos {fm(Calculo(p).diminuir(13))}')
