""""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar."""


resp = ''
soma = 0
cont = 0
maior = 0
menor = 0
media = 0
valor = 0
while resp != 'N':
    valor = int(input('Digite um valor: '))
    cont += 1
    soma += valor
    media = soma / cont
    if cont == 1:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()

print(f'A soma de todos os valores é: {soma}')
print(f'A média de todos os valores é: {media}')
print(f'O MENOR valor digitado é: {menor}')
print(f'O MAIOR valor digitado é: {maior}')






