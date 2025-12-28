from jogo import tabuleiro
print(tabuleiro)
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