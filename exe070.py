"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário deseja continuar.
No final, mostre:
A)Qual o total gasto na compra?
B)Quantos produtos custam mais de R$1000,00.
C)Qual o nome do produto mais barato?"""

resp = 'S'
soma = 0
cont = 0
menor = 0
menor_produto = ''
menor_preco = 0
while True:
    while resp == 'S':
        produto = str(input('Nome do produto: '))
        preco = float(input('Valor do produto: '))
        if menor_produto == '':
            menor = preco
            menor_produto = produto
            menor_preco = preco
        elif preco < menor:
            menor = preco
            menor_produto = produto
            menor_preco = preco
        soma += preco
        if preco > 1000:
            cont += 1
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
        while resp != 'S' and resp != 'N':
            resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-'*30)
print(f'TOTAL da compra ficou: R${soma:.2f}.')
print(f'{cont} produtos custam mais de R$1000.')
print(f'PRODUTO MAIS BARATO da lista é {menor_produto} custando R${menor_preco:.2f}.')

