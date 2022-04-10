'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso.
– Entre 18,5 e 25: Peso Ideal.
– 25 até 30: Sobrepeso.
– 30 até 40: Obesidade.
– Acima de 40: Obesidade Mórbida.'''

print('\033[7;49;33m** Vamos calcular seu IMC? **\033[m')
peso = float(input('\033[0;33m Digite seu peso em kg: \033[m'))
altura = float(input('\033[0;33m Digite sua altura em metro: \033[m'))
imc = peso / altura**2
print('\033[7;49;37m O seu IMC é {:.1f}. \033[m'.format(imc))

if imc <= 18.5:
    print('\033[1;31m Você está abaixo do peso.\033[m')
elif imc <= 25:
    print('\033[1;32m Seu peso está ideal.\033[m')
elif imc <= 30:
    print('\033[1;32m Você está com SOBREPESO. \033[m')
elif imc <= 40:
    print('\033[1;32m Você está com OBESIDADE. \033[m')
else:
    print('\033[1;31m CUIDADO!! Você está com OBESIDADE MÓRBIDA. \033[m')
    