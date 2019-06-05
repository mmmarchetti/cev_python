class Calculo:

    def __init__(self, num, cond=True):
        self.num = num
        self.cond = cond

    def metade(self):
        result = (self.num / 2)
        if self.cond:
            result = f'R${result:0.2f}'
        return result

    def dobro(self):
        result = self.num * 2
        if self.cond:
            result = f'R${result:0.2f}'
        return result

    def aumentar(self, porcent):
        result = self.num + (self.num * (porcent / 100))
        if self.cond:
            result = f'R${result:0.2f}'
        return result

    def diminuir(self, porcent):
        result = self.num - (self.num * (porcent / 100))
        if self.cond:
            result = f'R${result:0.2f}'
        return result
