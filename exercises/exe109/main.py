from exercises.exe109.moeda import Calculo
from exercises.exe108.moeda_ptbr import formata_moeda as fm

p = float(input('Digite o preço: R$'))
conta = Calculo(p, True)
print(f'A metade de {fm(p)} é {conta.metade()}')
print(f'O dobro de {fm(p)} é {conta.dobro()}')
print(f'Aumentando 10% temos {conta.aumentar(10)}')
print(f'Diminuindo 13%, temos {conta.diminuir(13)}')
