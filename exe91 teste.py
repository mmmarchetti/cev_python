from random import randint as rd
from time import sleep as sl
from operator import itemgetter as ig

jogo = {'jogador1': rd(1, 6), 'jogador2': rd(1, 6),
        'jogador3': rd(1, 6), 'jogador4': rd(1, 6)}

jogo_ord = sorted(jogo.items(), key=ig(1), reverse=True)

for k, v in jogo.items():
    print(f'{k}, {v}')
    sl(1)

jogo_ord = sorted(jogo.items(), key=ig(1), reverse=True)

for i, c in enumerate(jogo_ord):
    print(f'{i+1}º lugar, {c[0]} tirou {c[1]}')
