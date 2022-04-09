'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER
E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:

- 1 PARA BINÁRIO
- 2 PARA OCTAL
- 3 PARA HEXADECIMAL'''

# num = int(input('Digite um número: '))
# conversao = str(input('escolha a base de conversao: BINARIO, OCTAL, HEXADECIMAL: '))
# binario = format(num, 'b')
# octal = format(num, 'o')
# hexadecimal = format(num, 'x')

# if conversao == 'BINARIO':
#     print('A conversao de {} em BINARIO é {}'.format(num, binario))
# elif conversao == 'OCTAL':
#     print('A conversao de {} em OCTAL é {}'.format(num, octal))
# elif conversao == 'HEXADECIMAL':
#     print('A conversao de {} em HEXADECIMAL é {}'.format(num, hexadecimal))
# else:
#     print('Opção invalida')

#EXEMPLO DO GUANABARA:
num = int(input('\033[1;32m Digite um número inteiro: '))

print('''Escolha uma das bases para CONVERSÃO:\033[m
\033[1;31;47m [ 1 ] converter para BINÁRIO
 [ 2 ] converter para OCTAL
 [ 3 ] converter para HEXADECIMAL\033[m''')

opcao = int(input('\033[1;32m Sua opção:\033[m '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida')
