pessoas={'nome':'Gustado','sexo?':'sim', 'idade': 23}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas ['sexo?']
pessoas['nome']='Daniel'
pessoas['peso']= 107
for k in pessoas.keys():
       print(k)
for v in pessoas.values():
       print(v)
for kk, vv in pessoas.items():
       print(f'{kk}={vv}')