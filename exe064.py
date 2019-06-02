soma = 0
cont = 0
while True:
    n = int(input('Digite um número: [999 para parar]: '))
    if n != 999:
        soma = soma + n
        cont = cont + 1
    else:
        break
print(f'Você digitou {cont} números. A soma entre eles é {soma}')