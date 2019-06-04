cafe = ('Pão', 'R$1,00', 'Leite', 'R$2,50', 'Mamão', 'R$2,00', 'Pão de Queijo', 'R$1,50')
print('-=-' * 10)
print(' ' * 7, 'Café da Manhã')
print('-=-' * 10)
n = 1
for c in cafe[::2]:
    print(c, '-'*10, cafe[n])
    n = n + 2