lista=list()
while True:
    n=(int(input('Digite um valor para a lista: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adionado com sucesso...')
    else:
        print('\033[31mValor já existente na lista, ele não será adicionado novamente.\033[m')

    r=str(input('\033[32mDeseja adicionar outro valor? [S/N] \033[m')).upper()
    if r in 'Nn':
        break
lista.sort()
print(f'Os valores adicionados a lista foram: {lista}')