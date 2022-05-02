valores=list()
for va in range(0,5):
    valores.append(int(input('Digite um valor para adicionar a lista: ')))
print(f'NA LISTA TEMOS OS VALORES {valores}')
for c, v in enumerate(valores):
    print(f'NA POSIÇÃO {c} TEMOS O VALOR {v}')
print('cheguei ao final da lista')