"""Escreva um programa para aprovar um empréstimo bancário para compra de
uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
 em quantos anos ele vai pagar.

 Calculo o valor da prestação mensal, sabendo que ela não pode exceder 30%
 do salário ou então o empréstimo será negado."""

casa = float(input("Qual o valor da casa? R$"))
sal = float(input("Qual seu salário? R$"))
anos = int(input("Em quantos anos deseja pagar? "))

data = anos * 12
parc = casa / data
limite = sal * 30 / 100

print("\033[1;43m-------EMPRÉSTIMO BANCÁRIO---------\033[m")

if parc < limite :
    print("PARABÉNS PELA NOVA CONQUISTA")
    print("Seu empréstimo foi aprovado!")
    print("VAlOR TOTAL CASA: R${}".format(casa))
    print("VALOR PARCELA: R${:.2f}".format(parc))
    print("PAGAMENTO EM {} MESES/{} ANOS".format(data, anos))
elif parc > limite:
    print("\033[0;31mEMPRÉSTIMO NÃO APROVADO\033[m")
    print("PARCELA COMPROMETE MAIS QUE 30% DO SEU SALÁRIO")


