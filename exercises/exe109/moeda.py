class Calculo:

    def __init__(self, num, cond=True):
        self.cond = cond
        self.num = num

    def metade(self):
        result = self.num / 2
        if self.cond:
            result = f'R${self.num:0.2f}'
        return result

    def dobro(self):
        result = self.num * 2
        if self.cond:
            result = f'R${self.num:0.2f}'
        return result

    def aumentar(self, porcent):
        result = self.num + (self.num * (porcent / 100))
        if self.cond:
            result = f'R${self.num:0.2f}'
        return result

    def diminuir(self, porcent):
        result = self.num - (self.num * (porcent / 100))
        if self.cond:
            result = f'R${self.num:0.2f}'
        return result
