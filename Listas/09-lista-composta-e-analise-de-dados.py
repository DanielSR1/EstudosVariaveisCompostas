#NESSE EXERCICO CRIEI UM PROGRAM QUE REGISTRA O NOME E PESO DE CERTAS PESSOAS, E NO FINAL ELE APRESENTA O NOME DA PESSOA COM O MAIOR E MENOR PESO.
temp=list()
principal=list()
menor=maior=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal)==0:
        maior=menor=temp[1]
    else:
        if temp[1] > maior:
            maior=temp[1]
        if temp[1] < menor:
            menor=temp[1]
    principal.append(temp[:])
    temp.clear()
    r=str(input('Deseja continuar? [S/N] ')).upper()
    if r in 'Nn':
        break
print(f'Voce cadatrou o total de {len(principal)} pessoas')
print(f'O maior peso cadastrado foi {maior} Kg, o peso de', end=' ')
for p in principal:
    if p[1]==maior:
        print(f'{p[0]}')
print(f'O menor peso cadastrado foi {menor} kg, o peso de', end=' ')
for pp in principal:
    if pp[1]==menor:
        print(f'{pp[0]}' )