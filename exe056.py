"""Desenvolva um programa que leia o
nome, idade e sexo de 04 pessoas.
No final do programa, mostre:

- A média da idade do grupo:
- Qual é  nome do homem mais velho:
- Quantas mulheres tem menos de 20 anos:"""

media = 0
nome_homem = ''
maior = 0
mulheres_menores = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    media += idade
    if sexo == 'M':
        if idade >= maior:
            maior = idade
            nome_homem = nome
    if sexo == 'F':
        if idade < 20:
            mulheres_menores += 1


print('A média de idade do grupo é {:.0f} anos.'.format(media/4))

if nome_homem != '':
    print('O {} é o homem mais velho tendo {} anos.'.format(nome_homem, maior))
else:
    print('Nenhum homem foi informado')

print('Tem um total de {} mulheres com menos de 20 anos.'.format(mulheres_menores))




