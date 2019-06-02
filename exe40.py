lista = []
for n in range (0, 4):
     lista.append(float(input(f'Digite sua nota do {n + 1}º bimestre: ')))
print(lista)
soma = 0
cont = 0
for c in lista:
    soma = soma + c
    cont = cont + 1
    med = soma / cont    
print(f'A média do seu boletim é: {med:.2}.')