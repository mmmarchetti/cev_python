peso = float(input('Qual o seu peso (kg): '))
altura = float(input('Qual sua altura (m): '))
cimc = peso / (altura ** 2)
imc = ['Baixo Peso','Peso Normal', 'Sobre Peso']
if cimc < 18.5:
    print(f'Seu IMC é de {cimc:.1f}. Você tem {imc[0]}')
elif 18.5 <= cimc < 25:
    print(f'Seu IMC é de {cimc:.1f}. Você tem {imc[1]}')
elif cimc >= 25:
    print(f'Seu IMC é de {cimc:.1f}. você tem {imc[2]}')