saque = int(input('Valor do Saque: '))
cem = cinq = vinte = dez = cinco = 0
while saque >= 1000:
    cem = cem + 10
    saque = saque - 1000
while saque >= 50:
    cinq = cinq + 1
    saque = saque - 50
while saque >= 20:
    vinte = vinte + 1
    saque = saque - 20
while saque >= 10:
    dez = dez + 1
    saque = saque - 10
while saque >= 5:
    cinco = cinco + 1
    saque = saque - 5
print(f'{cem} notas de R$100,00')
print(f'{cinq} notas de R$50,00')
print(f'{vinte} notas de R$20,00')
print(f'{dez} notas de R$10,00')
print(f'{cinco} notas de R$5,00')