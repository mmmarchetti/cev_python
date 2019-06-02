sal = int(input('Digite o seu salário: R$'))
if sal > 1200:
    print(f'O seu salário após o reajuste será de: R${(sal * 0.05) + sal}')
else:
    print(f'O seu salário após o reajuste será de: R${(sal * 0.1) + sal}')