fundo_jogavel = '*  '
fundo_injogavel = '=  '
jogador = 'o  '
computador_ = 'x  '
tabuleiro = [
    ['X   ', 9, 0],
    ['8  ', 8, 0], [fundo_injogavel, 8, 1], [computador_, 8, 2], [fundo_injogavel, 8, 3], [computador_, 8, 4], [fundo_injogavel, 8, 5], [computador_, 8, 6], [fundo_injogavel, 8, 7], [computador_, 8, 8],
    ['7  ', 7, 0], [computador_, 7, 1], [fundo_injogavel, 7, 2], [computador_, 7, 3], [fundo_injogavel, 7, 4], [computador_, 7, 5], [fundo_injogavel, 7, 6], [computador_, 7, 7], [fundo_injogavel, 7, 8],
    ['6  ', 6, 0], [fundo_injogavel, 6, 1], [fundo_jogavel, 6, 2], [fundo_injogavel, 6, 3], [computador_, 6, 4], [fundo_injogavel, 6, 5], [computador_, 6, 6], [fundo_injogavel, 6, 7], [computador_, 6, 8],
    ['5  ', 5, 0], [fundo_jogavel, 5, 1], [fundo_injogavel, 5, 2], [jogador, 5, 3], [fundo_injogavel, 5, 4], [jogador, 5, 5], [fundo_injogavel, 5, 6], [fundo_jogavel, 5, 7], [fundo_injogavel, 5, 8],
    ['4  ', 4, 0], [fundo_injogavel, 4, 1], [fundo_jogavel, 4, 2], [fundo_injogavel, 4, 3], [fundo_jogavel, 4, 4],  [fundo_injogavel, 4, 5], [fundo_jogavel, 4, 6], [fundo_injogavel, 4, 7], [fundo_jogavel, 4, 8],
    ['3  ', 3, 0], [jogador, 3, 1], [fundo_injogavel, 3, 2], [fundo_jogavel, 3, 3], [fundo_injogavel, 3, 4],  [fundo_jogavel, 3, 5], [fundo_injogavel, 3, 6], [jogador, 3, 7], [fundo_injogavel, 3, 8],
    ['2  ', 2, 0], [fundo_injogavel, 2, 1], [jogador, 2, 2], [fundo_injogavel, 2, 3], [jogador, 2, 4], [fundo_injogavel, 2, 5], [fundo_jogavel, 2, 6], [fundo_injogavel, 2, 7], [jogador, 2, 8],
    ['1  ', 1, 0], [jogador, 1, 1], [fundo_injogavel, 1, 2], [jogador, 1, 3], [fundo_injogavel, 1, 4], [jogador, 1, 5], [fundo_injogavel, 1, 6], [jogador, 1, 7], [fundo_injogavel, 1, 8],
    ['0  ', 0, 0], ['1  ', 0, 0], ['2  ', 0, 0], ['3  ', 0, 0], ['4  ', 0, 0], ['5  ', 0, 0], ['6  ', 0, 0],  ['7  ', 0, 0], ['8  ', 0, 0], ['Y  ', 0, 0], ]

def tabuada():
    posicao = 0
    for c in tabuleiro:
        if posicao != c[1]:
            print()
        posicao = c[1]
        print(c[0], end='')
    print('')
    print('')

def jogada():

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

def computador():
    jogada = 0

    for c in tabuleiro:
        if c[0] == 'x  ' and jogada == 0:

            for v in tabuleiro:
                if c[1] - 1 == v[1] and c[2] - 1 == v[2] and v[0] == 'o  ' and jogada == 0:
                    v[0] = fundo_jogavel
                    for v in tabuleiro:
                        if c[1] - 2 == v[1] and c[2] - 2 == v[2] and v[0] == '*  ' :

                            for v in tabuleiro:
                                if c[1] - 3 == v[1] and c[2] - 3 == v[2] and v[0] == 'o  ' and jogada == 0:
                                    v[0] = fundo_jogavel
                                    for v in tabuleiro:
                                        if c[1] - 4 == v[1] and c[2] - 4 == v[2] and v[0] == '*  ':

                                            c[0] = '*  '
                                            v[0] = 'x  '
                                            jogada += 1
                                            break

                            for v in tabuleiro:
                                if c[1] - 3 == v[1] and c[2] - 1 == v[2] and v[0] == 'o  ' and jogada == 0:
                                    v[0] = fundo_jogavel
                                    for v in tabuleiro:
                                        if c[1] - 4 == v[1] and c[2] - 0 == v[2] and v[0] == '*  ':
                                            c[0] = '*  '
                                            v[0] = 'x  '
                                            jogada += 1
                                            break

                            for v in tabuleiro:
                                if c[1] - 1 == v[1] and c[2] - 3 == v[2] and v[0] == 'o  ' and jogada == 0:
                                    v[0] = fundo_jogavel
                                    for v in tabuleiro:
                                        if c[1] - 0 == v[1] and c[2] - 4 == v[2] and v[0] == '*  ':
                                            c[0] = '*  '
                                            v[0] = 'x  '
                                            jogada += 1
                                            break



    for c in tabuleiro:
        if c[0] == 'x  ' and jogada == 0:

            for v in tabuleiro:
                if c[1] - 1 == v[1] and c[2] - 1 == v[2] and v[0] == 'o  ':
                    v[0] = fundo_jogavel
                    for v in tabuleiro:
                        if c[1] - 2 == v[1] and c[2] - 2 == v[2] and v[0] == '*  ' :
                            c[0] = '*  '
                            v[0] = 'x  '
                            jogada += 1
                            break

                if c[1] - 1 == v[1] and c[2] + 1 == v[2] and v[0] == 'o  ':
                    v[0] = fundo_jogavel
                    for v in tabuleiro:
                        if c[1] - 2 == v[1] and c[2] + 2 == v[2] and v[0] == '*  ':
                            c[0] = '*  '
                            v[0] = 'x  '
                            jogada += 1
                            break

                if c[1] + 1 == v[1] and c[2] - 1 == v[2] and v[0] == 'o  ':
                    v[0] = fundo_jogavel
                    for v in tabuleiro:
                        if c[1] + 2 == v[1] and c[2] - 2 == v[2] and v[0] == '*  ':
                            c[0] = '*  '
                            v[0] = 'x  '
                            jogada += 1
                            break

                if c[1] + 1 == v[1] and c[2] + 1 == v[2] and v[0] == 'o  ':
                    v[0] = fundo_jogavel
                    for v in tabuleiro:
                        if c[1] + 2 == v[1] and c[2] + 2 == v[2] and v[0] == '*  ':
                            c[0] = '*  '
                            v[0] = 'x  '
                            jogada += 1
                            break

    for c in tabuleiro:
        if c[0] == 'x  ' and jogada == 0:

            for v in tabuleiro:
                if c[1] - 1 == v[1] and c[2] - 1 == v[2] and v[0] == '*  ':
                    c[0] = '*  '
                    v[0] = 'x  '
                    jogada += 1
                    break
                if c[1] - 1 == v[1] and c[2] + 1 == v[2] and v[0] == '*  ':
                    c[0] = '*  '
                    v[0] = 'x  '
                    jogada += 1
                    break
                if c[1] + 1 == v[1] and c[2] - 1 == v[2] and v[0] == '*  ':
                    c[0] = '*  '
                    v[0] = 'x  '
                    jogada += 1
                    break
                if c[1] + 1 == v[1] and c[2] + 1 == v[2] and v[0] == '*  ':
                    c[0] = '*  '
                    v[0] = 'x  '
                    jogada += 1
                    break

while True:
    tabuada()
    jogada()
    computador()
    tabuada()