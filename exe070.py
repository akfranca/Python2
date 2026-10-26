"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário deseja continuar.
No final, mostre:
A)Qual o total gasto na compra?
B)Quantos produtos custam mais de R$1000,00.
C)Qual o nome do produto mais barato?"""

resp = 'S'
soma = 0
cont = 0
while True:
    while resp == 'S':
        produto = str(input('Nome do produto: '))
        preco = float(input('Valor do produto: '))
        soma += preco
        if preco > 1000:
            cont += 1
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'O total da compra ficou: R${soma:.2f}.')
print(f'{cont} produtos custam mais de R$1000.')
print(f'O produto mais barato da lista é {produto} custando R${preco:.2f}.')


