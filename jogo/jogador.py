from dados import *

def tabuada():
    posicao = 0
    for c in tabuleiro:
        if posicao != c[1]:
            print()
        posicao = c[1]
        print(c[0], end='')
    print('')
    print('')

def jogador_():

    jogada_1 = 0
    while jogada_1 == 0:

        while True:
            while True:
                try:
                    posicao_x1 = int(input('x = '))
                except:
                    print('Digite um valor valido')
                else:
                    break
            if posicao_x1 >= 0 and posicao_x1 <= 9:
                break
            else:
                print('Digite um valor valido')

        while True:
            while True:
                try:
                    posicao_y1 = int(input('y = '))
                except:
                    print('Digite um valor valido')
                else:
                    break
            if posicao_y1 >= 0 and posicao_y1 <= 9:
                break
            else:
                print('Digite um valor valido')

        for c in tabuleiro:
            if c[1] == posicao_x1:
                if c[2] == posicao_y1:
                    if c[0] == 'o  ':
                        jogada_1 = c[:]
                        c[0] = '\033[35m{}\033[0m'.format(c[0])
                    else:
                        print('')
                        print('Posição invalida.')
                        print('')

    tabuada()

    jogada_2 = 0

    while jogada_2 == 0:
        print('')
        print('')

        while True:
            while True:
                try:
                    posicao_x2 = int(input('x2 = '))
                except:
                    print('Digite um valor valido')
                else:
                    break
            if posicao_x2 >= 1 and posicao_x2 <= 9:
                break
            else:
                print('Digite um valor valido')

        while True:
            while True:
                try:
                    posicao_y2 = int(input('y2 = '))
                except:
                    print('Digite um valor valido')
                else:
                    break
            if posicao_y2 >= 1 and posicao_y2 <= 9:
                break
            else:
                print('Digite um valor valido')

        for c in tabuleiro:
            if c[1] == posicao_x2:
                if c[2] == posicao_y2:
                    if c[0] == fundo_jogavel:
                        c[0] = 'o  '
                        jogada_2 = 1
                    else:
                        print(f'Espaço injogavel ')
                        print(f'x1 : {posicao_x1}, x2 : {posicao_x2}, y1 : {posicao_y1}, y2 : {posicao_y2}')
                        print(f'c[1]: {c[1]}, c[2]: {c[2]}. c[0]: {c[0]}, fundo: {fundo_jogavel}')


    for c in tabuleiro:
        if c[1] == posicao_x1:
            if c[2] == posicao_y1:
                c[0] = '*  '

# jogador()
# tabuada()
