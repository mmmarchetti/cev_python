print('Aprovador de empréstimos')
vcasa = int(input('Digite o valor do imóvel: '))
vsal = int(input('Digite o valor do seu salário: '))
parc = int(input('Digite a quantidade de parcelas: '))
if (vcasa / parc) <= (vsal * 0.3):
    print('Empréstimo aprovado.')
    print(f'A compra será feita em {parc} parcelas de R${(vcasa/parc)}, valor total de R${vcasa}.')
else:
    print('Empréstimo não aprovado.')
    