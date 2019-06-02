pessoas = int(input('Quantas pessoas tem o grupo? '))
sidade = 0
maior = 0
mulher20 = 0
nomev = ''
mf = ''
for c in range (1, pessoas + 1):
    print('-=' * 5, f'{c + 1}ª Pessoa', '-=' * 5)
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    sidade = sidade + i
    s = str(input('[M/F]: ')).upper()
    if c == 1:
        maior = i
        nomev = n
        if 'M' in s:
            mf = str('O Homem mais velho')
        elif 'F' in s:
            mf = str('A Mulher mais velha')
    if i > maior:
        maior = i 
        nomev = n
        if 'M' in s:
            mf = str('O Homem mais velho')
        elif 'F' in s:
            mf = str('A Mulher mais velha')
    if (s == 'F') and i < 20:
        mulher20 = mulher20 + 1
print(f'A média de idade do grupo é de {sidade / pessoas :.1f} anos.')
print(f'{mf} tem {maior} anos e se chama {nomev}.')
print(f'São {mulher20} mulheres com menos de 20.')