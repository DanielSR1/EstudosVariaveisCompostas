#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE ESCREVER PRO EXTERNSO O NÚMERO DIGITADO ENTRA 0 E 15.
conta=('zero','um','dois','três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez',
'onze','doze', 'treze', 'quatorze', 'quinze')
while True:
    num=int(input('\033[4mDigite um número entre 0 e 15: \033[m'))
    if 0<=num <=15:
        break
    print('TENTE NOVAMENTE, ENTRE 0 E 15: ')
print(f'Você digitou o número {conta[num]}')