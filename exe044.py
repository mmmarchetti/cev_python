print('-=' * 10, 'Loja Info', '-=' * 10)
p = int(input('Valor total da compra: R$'))
print("Formas de pagamento: "
"\n[1] à vista"
"\n[2] à vista no Cartão"
"\n[3] em até 10x no cartão")
while True:
    s = int(input('Qual é a opção desejada: '))
    if s == 1:
        print(f'Sua compra de R${p} vai sair {p - (p * 0.1)} à vista.')
        break
    elif s == 2:
        print(f'Sua compra de R${p} vai sair {p - (p *0.05)} à vista no cartão.')
        break
    elif s == 3:
        while True:
            v = int(input('Em quantas vezes quer parcelar? '))
            if v > 10:
                print('Parcelamos somente em até 10 vezes. Digite novamente.')
            else:
                print(f'Sua compra de R${p} vai sair em {v} de R${p / v :.2f}.' )
                break
        break
    else:
        print('Opção inválida')
        
           