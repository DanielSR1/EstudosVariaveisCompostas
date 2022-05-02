from os import remove
num=[2, 1 ,4 ,3 , 8]
num[3]=5
num.insert(4, 176)
num.append(7)
num.pop(3)
if 10 in num:
    num.remove(10)
else:
    print('não achei o número 10.')
print(num)
print(f'ESSA LISTA TEM {len(num)} ELEMENTOS.')