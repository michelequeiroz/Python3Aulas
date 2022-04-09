'''ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS,
MOSTRANDO NA TELA UMA MENSAGEM:

- O PRIMEIRO VALOR É MAIOR
- O SEGUNDO VALOR É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS'''

num1 = int(input('\033[1;34mPrimeiro número: '))
num2 = int(input('Segundo número: \033[m'))

if num1 > num2:
    print('O \033[0;32mPRIMEIRO\033[m valor é maior')
elif num2 > num1:
    print('O \033[0;32mSEGUNDO\033[m valor é maior')
else:
    print('\033[1;31m NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS \033[m')
    