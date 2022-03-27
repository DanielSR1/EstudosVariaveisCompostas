n1=(int(input('DIGITE UM NÚMERO: ')),
int(input('DIGITE OUTRO NÚMERO: ')),
int(input('DIGITE MAIS UM NÚMERO: ')),
int(input('DIGITE ÚLTIMO NÚMERO: ')))
print(f'VOCÊ DIGITOU OS VALORES {n1}')
print(f'O NÚMERO 9 APARECEU {n1.count(9)} VEZES.')
if 3 in n1:
    print(f'O VALOR 3 APARECEU NA {n1.index(3)+1} POSIÇÃO')
else:
    print('O VALOR 3 NÃO FOI DIGITADO')
print('OS VALORES PARES DIGITADOR FORAM', end=' ')
for n in n1:
    if n % 2==0:
        print(n, end=' ')

