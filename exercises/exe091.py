from random import randint as r
from time import sleep as s
jogadores = {'jogador1': r(1, 6), 'jogador2': r(1, 6),
             'jogador3': r(1, 6), 'jogador4': r(1, 6)}
for k, n in jogadores.items():
    s(1)
    print(f'{k} tirou {n} no dado.')
s(1)
print('-=-' * 20)
print('Ranking dos Jogadores:')
print(max(jogadores))