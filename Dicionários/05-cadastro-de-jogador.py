jog=dict()
partidas=list()
jog['nome']=str(input('NOME DO JOGADOR: '))
tot=int(input(f'Quantas partidas {jog["nome"]} jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols ele fez na {c+1}º partida : ')))
jog['gols']=partidas
jog['total']= sum(partidas)
print('-='*40)
print(jog)
print('-='*40)
for k, v in jog.items():
    print(f'o campo {k} tem valor {v}.')
print('-='*40)
for i, v in enumerate(jog['gols']):
    print(f'Na partida {i} fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols.')
