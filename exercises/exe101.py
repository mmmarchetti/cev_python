from datetime import date


def calc_idade(nascimento):
    hoje = date.today()
    ano_atual = hoje.year
    idade = ano_atual - nascimento
    return idade


def verifi_votacao(idade):
    if idade >= 18:
        print('Você tem idade para votar!')
    else:
        print('Você não pode votar!')


nasc = int(input('Digite o ano de seu nascimento [formato: XXXX]: '))
idade = calc_idade(nasc)
print(f'Você tem {idade} anos.')
verifi_votacao(idade)


