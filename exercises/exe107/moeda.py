class Calculo:

    def __init__(self, num):
        self.num = num

    def metade(self):
        return self.num / 2

    def dobro(self):
        return self.num * 2

    def aumentar(self, porcent):
        result = self.num + (self.num * (porcent / 100))
        return result

    def diminuir(self, porcent):
        result = self.num - (self.num * (porcent / 100))
        return result
