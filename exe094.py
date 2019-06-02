
dados_nomes = dict()
lista_pessoas = list()

while True:
    dados_nomes['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()
        if sexo in 'MF':
            dados_nomes['sexo'] = sexo
            break
        print('Erro! Por favor digite [M/F]')

    dados_nomes['idade'] = float(input('Idade: '))

    lista_pessoas.append(dados_nomes.copy())

    while True:
        continua = str(input('Deseja continuar [S/N]? ')).upper()
        if continua in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if continua == 'N':
        break

print(f'A) Ato todo temos {len(lista_pessoas)} pessoas.')

idade_tot = 0
for i in lista_pessoas:
    idade_tot = idade_tot + dados_nomes['idade']
med_idade = float(idade_tot / len(lista_pessoas))
print(f'A média de idade é de {med_idade}')

mulheres = []
cont = 0
for i in lista_pessoas:
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
        cont = cont + 1
if cont > 0:
    print(f'As mulheres cadastradas foram: ')
    for i in mulheres:
        print(f'{i}', end=' ')

print(lista_pessoas)
