"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado
(numero inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de
R$50.00, R$20.00, R$10.00 e R$1.00."""


print('-'*30)
print('CAIXA ELETRÔNICO')
print('-'*30)
saque = int(input('Qual valor deseja sacar? R$'))
cedula50 = saque // 50
saque = saque % 50
cedula20 = saque // 20
saque = saque % 20
cedula10 = saque // 10
saque = saque % 10
cedula1 = saque // 1
print('-'*30)
print(f'Cédula de R$50,00: {cedula50}')
print(f'Cédula de R$20,00: {cedula20}')
print(f'Cédula de R$10,00: {cedula10}')
print(f'Cédula de R$1,00: {cedula1}')
print('-'*30)

