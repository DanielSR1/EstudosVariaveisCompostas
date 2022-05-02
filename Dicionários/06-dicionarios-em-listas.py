pessoas=dict()
galera=list()
soma=media=0
while True: 
    pessoas.clear
    pessoas['nome']=str(input('Nome: ')).upper()
    while True:
        pessoas['estu']=str(input(f'{pessoas["nome"]} é estudante? [S/N] ')).upper()[0]
        if pessoas['estu'] in 'SN':
            break
        print('ERRO! ESCOLHA S OU N.')
    pessoas['idade']=int(input('Idade: '))
    soma=+soma+pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp=str(input('Deseja cadastrar outra pessoas? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! ESCOLHA S OU N.')
    if resp=='N':
        break
media=soma/len(galera)
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'A média das idades é de {media:5.2f}.')
print('Os estudantes cadastradas foram ', end=' ')
for p in galera:
    if p['estu']=='S':
        print(f'{p["nome"]}', end=' ')



