#Nesse exercicios desenvoli um programa capaz de ler a nota de um aluno e dizer se ele foi aprovado ou reprovado.
dados=dict()
dados['nome']=str(input('NOME: '))
dados['nota']=float(input('MÉDIA: '))
print(f'NOME É IGUAL A {dados["nome"]}.')
print(f'MÉDIA É IGUAL A {dados["nota"]}.')
print('-='*40)
if dados['nota'] < 7.0:
    print(f'SUA MÉDIA É {dados["nota"]}, REPROVADO.')
else:
    print(f'SUA MÉDIA É {dados["nota"]}, APROVADO!')
print(dados)