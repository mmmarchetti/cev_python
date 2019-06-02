print('Verificador de Triângulos')
l1 = int(input('Digite o valor de um lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do último lado: '))
if (l3 + l2) > l1 > (l3 - l2):
    print('Os lados formam um triângulo')
else:
    print('Os lados não formam um triângulo')