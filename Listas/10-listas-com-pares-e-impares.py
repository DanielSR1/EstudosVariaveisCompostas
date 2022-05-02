#Nesse exercicios criei um programa onde o usuário digita sete valores numéricos que são separados em uma lista única que mantenha separados os valores pares e ímpares em duas listas diferentes. após isso, valores são separados em pares e ímpares em ordem crescente.
valores=[[], []]
cont=0
for l in range(0,7):
    cont=(int(input('Digite o valor: ')))
    if cont%2==0:
        valores[0].append(cont)
    else:
        valores[1].append(cont)
valores[0].sort()
valores[1].sort()
print(f'Os número PARES digitados foram {valores[0]}')
print(f'Os números ÍMPARES digitados foram {valores[1]}')