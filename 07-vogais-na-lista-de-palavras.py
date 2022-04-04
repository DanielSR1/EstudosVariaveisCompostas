#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE DIZER QUAIS AS VOGAIS DE UMA PALAVRA EM UMA TUPLA.
palavras=('aprender', 'dinheiro', 'curso', 'teclado')
for p in palavras:
    print(f'\nNa palavras {p} temos as vogais:', end=' ')
    for letra in p:
        if letra.lower() in "aeiou":
            print(f'{letra}', end=' ')