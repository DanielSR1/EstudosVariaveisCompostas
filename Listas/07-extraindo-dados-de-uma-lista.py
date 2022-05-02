lista=list()
while True:
    n=(int(input("Digite um valor para adicionar a lista: ")))
    lista.append(n)
    r=str(input('Deseja continuar? [S/N] ')).upper()
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'Voce adicionou {len(lista)} valores a lista.')
print(f'A lista em ordem descresente é {lista}.')
if '5' in lista:
    print('O valor foi encontrado na lista.') 
else:
    print('O valor 5 não foi encontrado na lista.')

