continuar = 'S'
total = 0
mil = 0
menor = 0
menorp = ''
print('Loja Marchetti')
while continuar not in 'Nn':
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    total = total + preço
    if preço > 1000:
        mil = mil + 1
    if menor == 0:
        menor = preço
        menorp = nome
    elif preço < menor:
        menor = preço
        menorp = nome
    continuar = str(input('Quer continuar? [S/N] '))
print(f'O total foi de R${total}.')
print(f'Há {mil} produto custando mais de R$1.000,00.')
print(f'O produto mais barato foi {menorp} custando R${menor}.')