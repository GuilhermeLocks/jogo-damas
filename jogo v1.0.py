fundo_jogavel = '*  '
fundo_injogavel = '=  '
jogador = 'o  '
computador = 'x  '
azul = '\033[34m0  \033[0m'
magenta = '\033[35m1  \033[0m'
verde = '\033[32m2  \033[0m'
vermelho = '\033[31m3  \033[0m'
todos = [azul, magenta, verde, vermelho, computador]
tabuleiro = [
    ['X  ', 9, 0],
    ['8  ', 8, 0], [fundo_injogavel, 8, 1], [fundo_jogavel, 8, 2], [fundo_injogavel, 8, 3], [fundo_jogavel, 8, 4], [fundo_injogavel, 8, 5], [fundo_jogavel, 8, 6], [fundo_injogavel, 8, 7], [fundo_jogavel, 8, 8],
    ['7  ', 7, 0], [fundo_jogavel, 7, 1], [fundo_injogavel, 7, 2], [fundo_jogavel, 7, 3], [fundo_injogavel, 7, 4], [fundo_jogavel, 7, 5], [fundo_injogavel, 7, 6], [fundo_jogavel, 7, 7], [fundo_injogavel, 7, 8],
    ['6  ', 6, 0], [fundo_injogavel, 6, 1], [fundo_jogavel, 6, 2], [fundo_injogavel, 6, 3], [fundo_jogavel, 6, 4], [fundo_injogavel, 6, 5], [fundo_jogavel, 6, 6], [fundo_injogavel, 6, 7], [fundo_jogavel, 6, 8],
    ['5  ', 5, 0], [fundo_jogavel, 5, 1], [fundo_injogavel, 5, 2], [fundo_jogavel, 5, 3], [fundo_injogavel, 5, 4], [jogador, 5, 5], [fundo_injogavel, 5, 6], [jogador, 5, 7], [fundo_injogavel, 5, 8],
    ['4  ', 4, 0], [fundo_injogavel, 4, 1], [fundo_jogavel, 4, 2], [fundo_injogavel, 4, 3], [computador, 4, 4], [fundo_injogavel, 4, 5], [fundo_jogavel, 4, 6], [fundo_injogavel, 4, 7], [fundo_jogavel, 4, 8],
    ['3  ', 3, 0], [fundo_jogavel, 3, 1], [fundo_injogavel, 3, 2], [fundo_jogavel, 3, 3], [fundo_injogavel, 3, 4], [fundo_jogavel, 3, 5], [fundo_injogavel, 3, 6], [fundo_jogavel, 3, 7], [fundo_injogavel, 3, 8],
    ['2  ', 2, 0], [fundo_injogavel, 2, 1], [fundo_jogavel, 2, 2], [fundo_injogavel, 2, 3], [fundo_jogavel, 2, 4], [fundo_injogavel, 2, 5], [fundo_jogavel, 2, 6], [fundo_injogavel, 2, 7], [fundo_jogavel, 2, 8],
    ['1  ', 1, 0], [fundo_jogavel, 1, 1], [fundo_injogavel, 1, 2], [fundo_jogavel, 1, 3], [fundo_injogavel, 1, 4], [fundo_jogavel, 1, 5], [fundo_injogavel, 1, 6], [fundo_jogavel, 1, 7], [fundo_injogavel, 1, 8],
    ['0  ', 0, 0],  ['1  ', 0, 0], ['2  ', 0, 0], ['3  ', 0, 0], ['4  ', 0, 0], ['5  ', 0, 0], ['6  ', 0, 0], ['7  ', 0, 0], ['8  ', 0, 0], ['Y  ', 0, 0],                                                                                                                                                     ]
def tabuada():
    posicao = 0
    for c in tabuleiro:
        if posicao != c[1]:
            print()
        posicao = c[1]
        print(c[0], end='')
    print('')
    print('')
def jogador():
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
        break

    for c in tabuleiro:
        if c[1] == posicao_x1:
            if c[2] == posicao_y1:
                c[0] = '*  '

    for c in tabuleiro:
        if c[1] == posicao_x2:
            if c[2] == posicao_y2:
                c[0] = 'o  '
def computador():

    # limpa o tabuleiro
    for c in tabuleiro:
        if c[0] == azul:
            c[0] = 'x  '
        if c[0] == magenta:
            c[0] = 'x  '
        if c[0] == verde:
            c[0] = 'x  '
        if c[0] == vermelho:
            c[0] = 'x  '

    # verificar posições jogáveis e deixa azul
    for c in tabuleiro:
        if c[0] == 'x  ':
            posicao_x = c[1]
            posicao_y = c[2]

            for c in tabuleiro:

                if c[0] == '*  'and c[1] == posicao_x - 1 and c[2] == posicao_y - 1:

                    for c in tabuleiro:
                        if c[1] == posicao_x:
                            if c[2] == posicao_y:
                                if c[0] == 'x  ':
                                    c[0] = azul

                if c[0] == '*  'and c[1] == posicao_x - 1 and c[2] == posicao_y + 1:

                    for c in tabuleiro:
                        if c[1] == posicao_x:
                            if c[2] == posicao_y:
                                if c[0] == 'x  ':
                                    c[0] = azul

                if c[0] == '*  'and c[1] == posicao_x + 1 and c[2] == posicao_y - 1:

                    for c in tabuleiro:
                        if c[1] == posicao_x:
                            if c[2] == posicao_y:
                                if c[0] == 'x  ':
                                    c[0] = azul

                if c[0] == '*  'and c[1] == posicao_x + 1 and c[2] == posicao_y + 1:

                    for c in tabuleiro:
                        if c[1] == posicao_x:
                            if c[2] == posicao_y:
                                if c[0] == 'x  ':
                                    c[0] = azul

    # verificar posições que pega 1 peça e deixa magenta
    for c in tabuleiro:
        if c[0] in todos:
            posicao_x = c[1]
            posicao_y = c[2]

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 1 and c[2] == posicao_y - 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 2 and c[2] == posicao_y - 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = magenta

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x-1 and c[2] == posicao_y-1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x-2 and c[2] == posicao_y-2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = magenta

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 1 and c[2] == posicao_y + 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 2 and c[2] == posicao_y + 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = magenta

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 1 and c[2] == posicao_y + 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 2 and c[2] == posicao_y + 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = magenta

    # verificar posições que pega 2 peças e deixa verde
    for c in tabuleiro:
        if c[0] in todos:
            posicao_x = c[1]
            posicao_y = c[2]

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 3 and c[2] == posicao_y - 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 4 and c[2] == posicao_y - 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 3 and c[2] == posicao_y - 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 4 and c[2] == posicao_y - 0:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 1 and c[2] == posicao_y - 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 0 and c[2] == posicao_y - 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 3 and c[2] == posicao_y + 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 4 and c[2] == posicao_y + 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 3 and c[2] == posicao_y + 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 4 and c[2] == posicao_y + 0:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 1 and c[2] == posicao_y + 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 0 and c[2] == posicao_y + 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 1 and c[2] == posicao_y + 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 0 and c[2] == posicao_y + 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 3 and c[2] == posicao_y + 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 4 and c[2] == posicao_y + 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 3 and c[2] == posicao_y + 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 4 and c[2] == posicao_y + 0:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 3 and c[2] == posicao_y - 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 4 and c[2] == posicao_y - 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 1 and c[2] == posicao_y - 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 0 and c[2] == posicao_y - 4:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 3 and c[2] == posicao_y - 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 4 and c[2] == posicao_y + 0:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = verde

    # verificar posições que pega 3 peças e deixa vermelho
    for c in tabuleiro:
        if c[0] in todos:
            posicao_x = c[1]
            posicao_y = c[2]

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 5 and c[2] == posicao_y - 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 6 and c[2] == posicao_y - 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 5 and c[2] == posicao_y - 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 6 and c[2] == posicao_y - 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 3 and c[2] == posicao_y - 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 2 and c[2] == posicao_y - 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho


            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 5 and c[2] == posicao_y - 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 6 and c[2] == posicao_y - 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 5 and c[2] == posicao_y + 1:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 6 and c[2] == posicao_y + 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho


            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 1 and c[2] == posicao_y - 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 2 and c[2] == posicao_y - 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 1 and c[2] == posicao_y - 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 2 and c[2] == posicao_y - 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho


            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 5 and c[2] == posicao_y + 3:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 6 and c[2] == posicao_y + 2:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 5 and c[2] == posicao_y + 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 6 and c[2] == posicao_y + 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho


            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x - 1 and c[2] == posicao_y + 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x - 2 and c[2] == posicao_y + 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

            for c in tabuleiro:
                if c[0] == 'o  ' and c[1] == posicao_x + 1 and c[2] == posicao_y + 5:
                    for c in tabuleiro:
                        if c[0] == '*  ' and c[1] == posicao_x + 2 and c[2] == posicao_y + 6:

                            for c in tabuleiro:
                                if c[1] == posicao_x:
                                    if c[2] == posicao_y:
                                        if c[0] in todos:
                                            c[0] = vermelho

    tabuada()
while True:
    computador()
    jogador()