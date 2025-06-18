fundo = '= '
jogador = 'o '
computador = 'x '
tabuleiro = [
    [fundo, 8, 1], [computador, 8, 2], [fundo, 8, 3], [computador, 8, 4], [fundo, 8, 5], [computador, 8, 6], [fundo, 8, 7], [computador, 8, 8],
    [computador, 7, 1], [fundo, 7, 2], [computador, 7, 3], [fundo, 7, 4], [computador, 7, 5], [fundo, 7, 6], [computador, 7, 7], [fundo, 7, 8],
    [fundo, 6, 1], [computador, 6, 2], [fundo, 6, 3], [computador, 6, 4], [fundo, 6, 5], [computador, 6, 6], [fundo, 6, 7], [computador, 6, 8],
    [fundo, 5, 1], [fundo, 5, 2], [fundo, 5, 3], [fundo, 5, 4], [fundo, 5, 5], [fundo, 5, 6], [fundo, 5, 7], [fundo, 5, 8],
    [fundo, 4, 1], [fundo, 4, 2], [fundo, 4, 3], [fundo, 4, 4], [fundo, 4, 5], [fundo, 4, 6], [fundo, 4, 7], [fundo, 4, 8],
    [jogador, 3, 1], [fundo, 3, 2], [jogador, 3, 3], [fundo, 3, 4], [jogador, 3, 5], [fundo, 3, 6], [jogador, 3, 7], [fundo, 3, 8],
    [fundo, 2, 1], [jogador, 2, 2], [fundo, 2, 3], [jogador, 2, 4], [fundo, 2, 5], [jogador, 2, 6], [fundo, 2, 7], [jogador, 2, 8],
    [jogador, 1, 1], [fundo, 1, 2], [jogador, 1, 3], [fundo, 1, 4], [jogador, 1, 5], [fundo, 1, 6], [jogador, 1, 7], [fundo, 1, 8]
             ]

posicao = 0
for c in tabuleiro:
    if posicao != c[1]:
        print()
    posicao = c[1]
    print(c[0], end='')
