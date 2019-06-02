classe = dict()
classe['nome'] = str(input('Nome: '))
classe['média'] = float(input('Média: '))
if classe['média'] >= 6:
    classe['situação'] = 'Aprovado'
else:
    classe['situação'] = 'Reprovado'
print(classe)
print(('-=-'*20))
for c, n in classe.items():
    print(f'{c} é {n}')