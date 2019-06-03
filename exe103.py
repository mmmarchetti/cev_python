def verifica_jogador(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'

    print(f'O jogador {nome} fez {gols} gols no campeonato', end='')


nome_joga = str(input('Nome do joagador: '))
gols_joga = input('Quantidade de gols: ')

verifica_jogador(nome_joga, gols_joga)
