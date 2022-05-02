from datetime import date, datetime
dados=dict()
dados['nome']=str(input('NOME: '))
nasc=int(input('ANO DE NASCIMENTO: '))
dados['idade']=datetime.now().year-nasc
dados['carteira']=int(input('CARTEIRA DE TRABALHO (0 NÃO TEM): '))
if dados['carteira'] !=0:
    dados['contrat']=int(input('ANO DE CONTRATAÇÃO: '))
    dados['salario']=float(input('SALÁRIO: R$ '))
    dados['aposentadoria']= dados['idade'] + ((dados['contrat'] + 35) - datetime.now().year)
print('-='*35)
for k, v in dados.items():
    print(f'- {k} tem valor {v}.')
