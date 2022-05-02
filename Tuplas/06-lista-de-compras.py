lista=('caderno', 15.50,
'mochila', 12.55,
'kit de escrever', 23.44,
'livros', 23.44)
for pos in range(0, len(lista)):
    if pos % 2==0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]:>5.2f}')