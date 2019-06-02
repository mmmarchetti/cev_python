from random import randint as r
from time import sleep as s
from operator import itemgetter as ig

players = {'jogador1': r(1, 6), 'jogador2': r(1, 6),
           'jogador3': r(1, 6), 'jogador4': r(1, 6)}
rkg_dict = dict()
print('Valores sorteados:')

for k, v in players.items():
    s(1)
    print(f'{k} tirou {v} no dado.')

print('-='* 30)
s(1)
print('Vencedores:')

rkg_dict = sorted(players.items(), key=ig(1), reverse=True)

for i, v in enumerate(rkg_dict):
    print(f'{v[0]} tirou {v[1]}, ficou em {i+1}º lugar')
    s(1)