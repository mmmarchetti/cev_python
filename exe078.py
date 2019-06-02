num = list()
for n in range(0, 5):
    while True:
        dig = input(f'Digite um valor na posição {n}: ').upper()
        if not dig.isdigit():
            print('Digite apenas numeros!')
        else:
            num.append(dig)
            break
print('-=-'*20)
print('Você digitou os valores: ',end=' ')
for c in num:
    print(c, end='...')
print(f'\nO maior valor digitado foi {max(num)}, na posição: ')
print(f'O menor valor digitado foi {min(num)}, na posição: ')