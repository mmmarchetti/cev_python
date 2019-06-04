def calc_area(larg, comp):
    resultado = larg * comp
    print(f'A area de um terreno de {larg} por {comp} é igual a {resultado} m²')


print('Controle de terrenos: ')
largura = int(input('Largura em metros: '))
comprimento = int(input('Comprimentro em metros: '))

calc_area(largura, comprimento)
