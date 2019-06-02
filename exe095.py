jogadores = {'nome': '', 'gols': []}
time = []
gols = []
while True:
    jogadores['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for partida in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {partida+1}: ')))
    jogadores['gols'] = gols[:]
    gols.clear()
    time.append(jogadores.copy())

    cont = str(input('Quer continuar [S/N]? ')).upper()
    if cont == 'N':
        break

print('-=-'*10)
print('cod  nome                gols            total')
for jogador in time:
    print(f'     {jogador["nome"]}        {jogador["gols"]}      {sum(jogador["gols"])}')

while True:
    cont = int(input('Mostrar dados de qual jogador? \n[999] para parar:'))
    if cont == 999:
        break
    try:
        for gol in time[cont]['gols']:
            print(f'No jogo fez {gol}')

    except IndexError:
        print('Digite um jogador válido')
        continue


