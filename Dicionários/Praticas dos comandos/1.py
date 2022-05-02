estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input('UNIDADE FEDERATIVA: '))
    estado['sigla']=str(input('SIGLA DO ESTADO: '))
    brasil.append(estado.copy())
print(brasil)
print('-='*30)
for e in brasil:
    print(e)
    for k, v in estado.items():
        print(f'O CAMPO {k} TEM VALOR {v}.')