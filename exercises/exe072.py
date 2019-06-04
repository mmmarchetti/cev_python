num = ('zero', 'um', 'dois', 'três',
       'quatro', 'cinco')
usu = int(input('Digite um número entre 0 e 5: '))
while True:
    if usu >= 0 and usu <= 5:
        print(num[usu])
        break
    else:
        usu = int(input('Digite um número entre 0 e 5: '))