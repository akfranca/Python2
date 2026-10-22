"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final mstre quantos números foram digitados,
e qual foi a soma entre eles."""


res = 0
cont = 0
soma = 0
while res != 999:
    res = int(input('Digite um número: '))
    if res != 999:
        cont += 1
        soma += res
print('Você digitou {} números e a soma entre eles é: {}'.format(cont, soma))



