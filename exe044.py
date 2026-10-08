"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

-à vista dinheir/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% juros"""

preço = float(input('Valor das compras: R$'))
print("""ESCOLHA FORMA DE PAGAMENTO
[1] À VISTA DINHEIRO/CHEQUE
[2] À VISTA CARTÃO
[3] 2X CARTÃO
[4] 3X OU MAIS CARTÃO""")
menu = int(input('Qual melhor opção para você? '))

if menu == 1:
 pgt1 = preço - (preço * 10 / 100)
 print('Você ganhou 10% de desconto e sua compra sairá por R${}'.format(pgt1))
elif menu == 2:
 pgt2 = preço - (preço * 5 / 100)
 print('Você ganhou 5% de desconto e sua compra sairá por R${}'.format(pgt2))
elif menu == 3:
    pgt3 = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(pgt3))
elif menu == 4:
    parc = int(input('Quantas parcelas? '))
    juros =  preço + (preço * 20 / 100)
    pgt4 = juros / parc
    print('Sua compra será parcelada em {}x de R${:.2f} com o juros de 20% o total de sua compra sairá por R${}'.format(parc, pgt4, juros))









