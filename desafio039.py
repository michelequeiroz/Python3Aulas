'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E 
INFORME, DE ACORDO COM SUA IDADE:

- SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
- SE É A HORA DE SE ALISTAR.
- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO

SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU 
QUE PASSOU DO PRAZO'''

from datetime import date
atual = date.today().year

nascimento = int(input('Seu ano de nascimento: '))
idade = atual - nascimento 
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))


if idade == 18:
    print('VOCÊ TEM QUE SE ALISTAR \033[0;31mIMEDIATAMENTE\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('VOCÊ AINDA NÃO TEM 18 ANOS. FALTA {} ANOS PARA O ALISTAMENTO!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('\033[1;33mVOCÊ JÁ DEVERIA TER SE ALISTADO A {} ANOS.\033[m'.format(saldo))

    