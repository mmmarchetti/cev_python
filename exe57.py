sexo = input('Digite o seu sexo [M/F]: ').upper()
while sexo not in 'FfMm':
    sexo = input('Dados inválidos. Digite o seu sexo [M/F]: ').upper()
print(f'Sexo {sexo} registrado com sucesso.')