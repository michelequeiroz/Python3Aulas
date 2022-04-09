'''ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA
A COMPRA DE UMA CASA.
O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR
E EM QUANTOS ANOS ELE VAI PAGAR

CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER
30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.'''

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
    