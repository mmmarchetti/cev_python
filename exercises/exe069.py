continuar = 's'
idade18 = 0
homens = 0
mulher20 = 0
while continuar in 'Ss':
    print('-=' * 20)
    print('Cadastre uma pessoa')
    print('-=' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    if idade > 18:
        idade18 = idade18 + 1
    if sexo in 'Mm':
        homens = homens + 1
    if sexo in 'Ff' and idade < 20:
        mulher20 = mulher20 + 1
    continuar = str(input('Quer continuar? [S/N]: '))
print(f'Total de pessoas com mais de 18: {idade18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')