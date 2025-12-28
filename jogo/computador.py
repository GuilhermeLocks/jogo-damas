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

def computador():
    jogada = 0

    for c in tabuleiro:
        if c[0] == 'x  ':

            for v in tabuleiro:

                if c[1] - 1 == v[1] and c[2] - 1 == v[2] and v[0] == '*  ':
                    c[0] = azul
                if c[1] - 1 == v[1] and c[2] + 1 == v[2] and v[0] == '*  ':
                    c[0] = azul
                if c[1] + 1 == v[1] and c[2] - 1 == v[2] and v[0] == '*  ':
                    c[0] = azul
                if c[1] + 1 == v[1] and c[2] + 1 == v[2] and v[0] == '*  ':
                    c[0] = azul

            for v in tabuleiro:

                if c[1] - 1 == v[1] and c[2] - 1 == v[2] and v[0] == 'o  ':
                    for v in tabuleiro:
                        if c[1] - 2 == v[1] and c[2] - 2 == v[2] and v[0] == '*  ' :
                            c[0] = magenta

                if c[1] - 1 == v[1] and c[2] + 1 == v[2] and v[0] == 'o  ':
                    for v in tabuleiro:
                        if c[1] - 2 == v[1] and c[2] + 2 == v[2] and v[0] == '*  ':
                            c[0] = magenta

                if c[1] + 1 == v[1] and c[2] - 1 == v[2] and v[0] == 'o  ':
                    for v in tabuleiro:
                        if c[1] + 2 == v[1] and c[2] - 2 == v[2] and v[0] == '*  ':
                            c[0] = magenta

                if c[1] + 1 == v[1] and c[2] + 1 == v[2] and v[0] == 'o  ':
                    for v in tabuleiro:
                        if c[1] + 2 == v[1] and c[2] + 2 == v[2] and v[0] == '*  ':
                            c[0] = magenta

    for c in tabuleiro:
        if c[0] == magenta and jogada == 0:
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
        if c[0] == azul and jogada == 0:
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



    for c in tabuleiro:
        if c[0] == azul:
            c[0] = 'x  '
        if c[0] == magenta:
            c[0] = 'x  '
        if c[0] == verde:
            c[0] = 'x  '
        if c[0] == vermelho:
            c[0] = 'x  '

computador()
tabuada()