soma = 0
cont = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
    if maior == 0:
        maior = num
    elif num > maior:
        maior = num
    if menor == 0:
        menor = num
    elif num < menor:
        menor = num
    continua = str(input('Quer continuar [S/N]: '))
    if continua in 'Nn':
        break
print(f'Você digitou {cont} números.')
print(f'A média entre eles é de {soma / cont:.1f}.')
print(f'O maior valor digitado foi o {maior} e o menor foi {menor}.')