palavras = ('AMO', 'DEMAIS', 'FRAN')
for p in palavras:
    print('A palavra {} tem as vogais' .format(p), end = ' ')
    for vogal in p:
        if vogal in 'AEIOU':
            print('{}' . format(vogal), end = ' ')
    print('')