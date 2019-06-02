listagem = ('Pão', 5.10, 'Leite', 2.25, 'Café', 1.50, 'Mamão', 3.75)
print('-=' * 20)
print(f'Café da manhã')
print('-=' * 20)
for c in range(0, len(listagem) - 1, 2):
    print(f'{listagem[c]}', '-' * 20, f'> R${listagem[c + 1]}')