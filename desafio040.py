'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO

- Média entre 5.0 e 6.9: RECUPERAÇÃO

- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Qual foi a 1° nota: '))
nota2 = float(input('Qual foi a 2° nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[1;34mREPROVADO! Sua média foi {:.2f} \033[m]'. format(media))

elif media >= 7.0:
    print('\033[1;32mAPROVADO! Sua média foi {:.2f} \033[m]'. format(media))

else:
    print('\033[1;35mRECUPERAÇÃO! Sua média foi {:.2f} \033[m]'. format(media))
