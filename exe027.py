nome = str(input('Digite o seu nome completo: ')).strip().upper()
nomediv = nome.split()
print('Seu primeiro nome {} é muito bonito!' .format(nomediv[0]))
if 'SILVA' in nomediv:
    print('Silva é um nome comum no Brasil')
else:
    print('Seu último nome {} é diferente!' .format(nomediv[-1]))
print('-Fim-')