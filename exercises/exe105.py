def notas(*num, sit=True):
    dados = {'total': 0, 'maior': 0, 'menor': 0, 'media': 0}
    soma = total = maior = 0
    menor = 100
    for n in num:
        total += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n
    media = soma / total

    dados['total'] = total
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = media

    if sit:
        if dados['media'] < 6:
            dados['situação'] = 'Ruim'
        else:
            dados['situação'] = 'Boa'
    return dados


result = notas(10, 8, 9, sit=False)
print(result)
