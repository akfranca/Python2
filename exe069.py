"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada o programa deverá perguntar se o usuário
quer continuar ou não. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

somai = 0
somah = 0
somaf = 0

while True:
    resp = 'S'
    sexo = ''
    while resp == 'S':
        print('-' * 30)
        print('CADASTRO DE USUÁRIO')
        print('-' * 30)
        idade = int(input('IDADE: '))
        sexo = str(input('SEXO:[F/M] ')).upper().strip()
        while sexo != 'F' and sexo != 'M':
            sexo = str(input('SEXO:[F/M] ')).upper().strip()
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
        while resp != 'S' and resp != 'N':
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if idade > 18:
            somai += 1
        if sexo == 'M':
            somah += 1
        if sexo == 'F' and idade < 20:
            somaf += 1
    if resp == 'N':
        break
print('-' * 30)
print(f'Há {somai} pessoas cadastradas com mais de 18 anos.')
print(f'Há um total de {somah} homens cadastrados.')
print(f'Há {somaf} mulheres com menos de 20 anos.')


