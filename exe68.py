from random import randint as r
jogadas = 3
scorepc = 0
scorepl = 0
while jogadas != 0:
    pc = r(1, 10)
    num = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar [P/I]: '))
    if (num + pc) % 2 == 0 and escolha in 'Pp':
        print('-=' * 20)
        print(f'Você jogou {num} e o computador {pc}. Total {num+pc} deu PAR')
        print('-=' * 20)
        print('Você ganhou!.')
        jogadas = jogadas - 1
        scorepl = scorepl + 1
    elif (num + pc) % 2 == 0 and escolha in 'Ii':
        print('-=' * 20)
        print(f'Você jogou {num} e o computador {pc}. Total {num+pc} deu PAR')
        print('-=' * 20)
        print('Você Perdeu!.')
        jogadas = jogadas - 1
        scorepc = scorepc + 1
    elif (num + pc) % 3 == 0 and escolha in 'Pp':
        print('-=' * 20)
        print(f'Você jogou {num} e o computador {pc}. Total {num+pc} deu ÍMPAR')
        print('-=' * 20)
        print('Você Perdeu!.')
        jogadas = jogadas - 1
        scorepc = scorepc + 1
    elif (num + pc) % 3 == 0 and escolha in 'Ii':
        print('-=' * 20)
        print(f'Você jogou {num} e o computador {pc}. Total {num+pc} deu ÍMPAR')
        print('-=' * 20)
        print('Você ganhou!.')
        jogadas = jogadas - 1
        scorepl = scorepl + 1
print('-=' * 20)
if scorepc > scorepl:
    print('Melhor de 3 e Você Perdeu!')
elif scorepc < scorepl:
    print('Melhor de 3 e Você ganhou!')
print('-=' * 20)
print(f'Game Over. Você ganhou {scorepl} vezes.')