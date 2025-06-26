fundo_jogavel = '=  '
fundo_injogavel = '*  '
jogador = 'o  '
computador = 'x  '

tabuleiro = [
    ['X  ', 9, 0],
    ['8  ', 8, 0], [fundo_jogavel, 8, 1], [computador, 8, 2], [fundo_jogavel, 8, 3], [computador, 8, 4], [fundo_jogavel, 8, 5], [computador, 8, 6], [fundo_jogavel, 8, 7], [computador, 8, 8],
    ['7  ', 7, 0], [computador, 7, 1], [fundo_jogavel, 7, 2], [computador, 7, 3], [fundo_jogavel, 7, 4], [computador, 7, 5], [fundo_jogavel, 7, 6], [computador, 7, 7], [fundo_jogavel, 7, 8],
    ['6  ', 6, 0], [fundo_jogavel, 6, 1], [computador, 6, 2], [fundo_jogavel, 6, 3], [computador, 6, 4], [fundo_jogavel, 6, 5], [computador, 6, 6], [fundo_jogavel, 6, 7], [computador, 6, 8],
    ['5  ', 5, 0], [fundo_injogavel, 5, 1], [fundo_jogavel, 5, 2], [fundo_injogavel, 5, 3], [fundo_jogavel, 5, 4], [fundo_injogavel, 5, 5], [fundo_jogavel, 5, 6], [fundo_injogavel, 5, 7], [fundo_jogavel, 5, 8],
    ['4  ', 4, 0], [fundo_jogavel, 4, 1], [fundo_injogavel, 4, 2], [fundo_jogavel, 4, 3], [fundo_injogavel, 4, 4], [fundo_jogavel, 4, 5], [fundo_injogavel, 4, 6], [fundo_jogavel, 4, 7], [fundo_injogavel, 4, 8],
    ['3  ', 3, 0], [jogador, 3, 1], [fundo_jogavel, 3, 2], [jogador, 3, 3], [fundo_jogavel, 3, 4], [jogador, 3, 5], [fundo_jogavel, 3, 6], [jogador, 3, 7], [fundo_jogavel, 3, 8],
    ['2  ', 2, 0], [fundo_jogavel, 2, 1], [jogador, 2, 2], [fundo_jogavel, 2, 3], [jogador, 2, 4], [fundo_jogavel, 2, 5], [jogador, 2, 6], [fundo_jogavel, 2, 7], [jogador, 2, 8],
    ['1  ', 1, 0], [jogador, 1, 1], [fundo_jogavel, 1, 2], [jogador, 1, 3], [fundo_jogavel, 1, 4], [jogador, 1, 5], [fundo_jogavel, 1, 6], [jogador, 1, 7], [fundo_jogavel, 1, 8],
    ['0  ', 0, 0],  ['1  ', 0, 0], ['2  ', 0, 0], ['3  ', 0, 0], ['4  ', 0, 0], ['5  ', 0, 0], ['6  ', 0, 0], ['7  ', 0, 0], ['8  ', 0, 0], ['Y  ', 0, 0],                                                                                                                                                     ]

def jogador():
    posicao = 0
    for c in tabuleiro:
        if posicao != c[1]:
            print()
        posicao = c[1]
        print(c[0], end='')
    print('')
    print('')
    posicao = 0
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
    for c in tabuleiro:
        if posicao != c[1]:
            print()
        posicao = c[1]
        print(c[0], end='')
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
            if c[0] == '*  ' and c[1] == posicao_x2 and c[
                2] == posicao_y2 and posicao_y1 + 2 == posicao_y2 and posicao_x1 + 2 == posicao_x2:
                jogada_2 = c[:]
                c[0] = '\033[34m{}\033[0m'.format(c[0])
            if c[0] == '*  ' and c[1] == posicao_x2 and c[
                2] == posicao_y2 and posicao_y1 + 2 == posicao_y2 and posicao_x1 - 2 == posicao_x2:
                jogada_2 = c[:]
                c[0] = '\033[34m{}\033[0m'.format(c[0])
            if c[0] == '*  ' and c[1] == posicao_x2 and c[
                2] == posicao_y2 and posicao_y1 - 2 == posicao_y2 and posicao_x1 - 2 == posicao_x2:
                jogada_2 = c[:]
                c[0] = '\033[34m{}\033[0m'.format(c[0])
            if c[0] == '*  ' and c[1] == posicao_x2 and c[
                2] == posicao_y2 and posicao_y1 - 2 == posicao_y2 and posicao_x1 + 2 == posicao_x2:
                jogada_2 = c[:]
                c[0] = '\033[34m{}\033[0m'.format(c[0])

            if c[0] == '*  ' and c[1] == posicao_x2 and c[
                2] == posicao_y2 and posicao_y1 - 1 == posicao_y2 and posicao_x1 + 1 == posicao_x2:
                jogada_2 = c[:]
                c[0] = '\033[34m{}\033[0m'.format(c[0])
            if c[0] == '*  ' and c[1] == posicao_x2 and c[
                2] == posicao_y2 and posicao_y1 + 1 == posicao_y2 and posicao_x1 + 1 == posicao_x2:
                jogada_2 = c[:]
                c[0] = '\033[34m{}\033[0m'.format(c[0])
    for c in tabuleiro:
        if c[1] == posicao_x1:
            if c[2] == posicao_y1:
                c[0] = '*  '
    for c in tabuleiro:
        if c[1] == posicao_x2:
            if c[2] == posicao_y2:
                c[0] = 'o  '

def computador():
    for c in tabuleiro:
        if c[0] == 'x  ':
            posicao_x = c[1]
            posicao_y = c[2]
            for v in tabuleiro:
                if v[0] == 'o  'and v[1] == posicao_x-1 and v[2] == posicao_y-1:
                    print(v)
                    print(c)
                    for c in tabuleiro:
                        if c[1] == posicao_x:
                            if c[2] == posicao_y:
                                if c[0] == 'x  ':
                                    c[0] = '\033[35m{}\033[0m'.format(c[0])

while True:
    jogador()
    computador()