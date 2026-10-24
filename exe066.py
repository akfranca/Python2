"""Crie um programaque leia vários números inteiros pelo teclado.
O programa só vai parar quando o usário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)."""


n = s = cont = 0
while True:
    n = int(input('Digite um número ou (use 999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} valores e a soma entre eles é: {s}...')
