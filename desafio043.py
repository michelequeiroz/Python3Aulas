'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

print('\033[0;32m Vamos calcular seu IMC? \033[m')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metro: '))

imc = peso / altura**2
print('O seu IMC é {:.1f}.'.format(imc))


















