"""Crie um programa que leia o sexo de uma pessoa,
mas que aceite somente os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter
um valor correto."""

resp = 'n'
while resp not in 'MF':
    resp = str(input('Qual seu sexo? [M/F]: ')).strip().upper()
    if resp == 'M':
        print('Sexo Masculino')
    if resp == 'F':
        print('Sexo Feminino')
    if resp != 'M' and resp != 'F':
        print('Sexo inválido, tente novamente.')

print('Obrigada pela resposta, volte sempre!')







