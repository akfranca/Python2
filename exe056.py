"""Desenvolva um programa que leia o
nome, idade e sexo de 04 pessoas.
No final do programa, mostre:

- A média da idade do grupo:
- Qual é  nome do homem mais velho:
- Quantas mulheres tem menos de 20 anos:"""

menor = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
if sexo == 'M':
    maior = idade
    menor = idade
if sexo == 'F' and idade < 20:
    maior = idade
    menor = idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

print('{} é o homem mais velho e ele tem {} anos.'.format(nome, maior))



