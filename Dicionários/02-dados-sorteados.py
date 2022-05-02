#Nesse erxercicio desenvolvi um programa capaz de rodas um dado de 6 lados para 4 jogadores e dizer quem fez mais pontos
from time import sleep
from random import randint
from operator import itemgetter
jogo={'JOGADOR 1':randint(1,6),
      'JOGADOR 2': randint (1,6),
      'JOGADOR 3': randint (1,6),
      'JOGADOR 4': randint (1,6)}
ranking=list()
print('VALORES SORTEADOS NO DADO')
sleep(0.5)
for k,v in jogo.items():
    print(f'{k} TIROU O NÚMERO {v} NO DADO')
    sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(ranking):
    print(f'\033[32mEm {i+1} LUGAR : {v[0]} COM {v[1]} PONTOS')