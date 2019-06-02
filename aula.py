print('Vamos Brincar!!!')
a = 1
cont = 0
while (a % 2) != 0:
    a = int(input('Digite um número par: '))
    if (a % 2) ==0:
        b = int(input('Até que número devemos multiplicar?'))
        for i in range(1, b+1):
            print(a, '*', i, '=', a*i)
    else:
        cont = cont + 1
        if cont == 1:
            print('Mas o número digitado não é par...tente novamente!')
        elif cont == 2:
            print(' Preste atenção!!! Digite outro número...')
        elif cont == 3:
            print('Você não está muito bem...mais uma chance!!!')
        elif cont == 4:
            print('Estou ficando sem paciência...vai lá e acerte esse número!!!')
        elif cont == 5:
            print('Melhor você ir estudar e voltar em outra oportunidade. Beijinhos!!!')
        else:
            break







