peso = []
pessoas = int(input('Digite a quantidade de pessoas: '))
for c in range (0, pessoas):
    peso.append(float(input(f'Peso da {c + 1}ª pessoa: ')))
print(f'O maior peso lido foi de {max(peso)}.')
print(f'O menor peso lido foi de {min(peso)}.')