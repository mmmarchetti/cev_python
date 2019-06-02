classe = list()
temp = []
aluno = list()
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append((temp[1] + temp[2]) / 2)
    aluno = temp[:]
    temp.clear()
    classe.append(aluno)
    continua = str(input('Quer continuar? [S/N]: '))
    if continua in 'Nn':
        break
print('-=-'*10)
print('Nº     Nome     Média')
print('-'*30)
for i, l in enumerate(classe):
    print(f'{i}      {l[0]}        {l[3]}')
print()
while True:
    print('Para parar digite 999.')
    verifican = int(input('Digite o número do aluno para verificar notas: '))
    if verifican == 999:
        break
    print()
    print(f'Aluno: {classe[verifican][0]}, Nota1: {classe[verifican][1]}, Nota 2: {classe[verifican][2]}')