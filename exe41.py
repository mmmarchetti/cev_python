idade = int(input('Digite a idade: '))
clas = ('Júnior', 'Mirim', 'Infantil', 'Master', 'Senior')
f = ('É jogador')
if idade <= 10:
    print(f'{f} {clas[0]}.')
elif 18 >= idade >= 11:
    print(f'{f} {clas[1]}.')
elif 25 >= idade > 18:
    print(f'{f} {clas[2]}.')
elif 30 >= idade > 25:
    print(f'{f} {clas[3]}.')
elif idade >= 40:
    print(f'{f} {clas[4]}.')