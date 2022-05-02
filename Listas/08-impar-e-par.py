#Nesse exercicio desenvolvi um programa que vai ler vários números e coloca-los em uma lista. Depois disso, ele separa em duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostra o conteúdo das três listas geradas.
lista=list()
par=list()
impar=list()
while True:
    n=int(input('Digite um valor para adicionar a lista: '))
    lista.append(n)
    r=str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
for p, v in enumerate(lista):
    if v % 2==0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista gerada foi {lista}')
print(f'Os valores impares na lista são {impar};')
print(f'Os valores pares na lista são {par}.')
