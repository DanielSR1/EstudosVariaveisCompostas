lista=list() 
for c in range (0,5):
    lista.append(int(input(f'Digite um valor numérico para adicionar a lista na {c} posição: ')))
print(f'A lista gerada foi: {lista}.')
print(f'O maior valor na lista é {max(lista)}.')
print(f'O menor valor na lista é {min(lista)}.')


    