class Calculo:

    def __init__(self, num, aum=0, dim=0, cond=True):
        self.num = num
        self.aum = aum
        self.dim = dim
        self.cond = cond

    def conta(self):
        result_metade = (self.num / 2)
        if self.cond:
            result_metade = f'R${result_metade:0.2f}'

        result_dobro = self.num * 2
        if self.cond:
            result_dobro = f'R${result_dobro:0.2f}'

        result_aumento = self.num + (self.num * (self.aum / 100))
        if self.cond:
            result_aumento = f'R${result_aumento:0.2f}'

        result_diminui = self.num - (self.num * (self.dim / 100))
        if self.cond:
            result_diminui = f'R${result_diminui:0.2f}'

        print(f'Preço analisado: R${self.num:0.2f}')
        print(f'Dobro do preço: {result_dobro}')
        print(f'Metade do preço: {result_metade}')
        print(f'{self.aum}% de aumento: {result_aumento}')
        print(f'{self.dim}% de reduação: {result_diminui}')

