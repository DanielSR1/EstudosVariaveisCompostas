from random import randint
print('ESSE É UM PROGRAMA QUE SORTEIA 5 VALORES ENTRE 1 E 10 E LOCALIZA O MAIOR E MENOR VALOR ENTRE ELES:')
num=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor entre eles é {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
