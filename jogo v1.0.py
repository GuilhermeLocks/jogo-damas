fundo_jogavel = '=  '
fundo_injogavel = '*  '
jogador = 'o  '
computador = 'x  '
tabuleiro = [
    [fundo_jogavel, 8, 1], [computador, 8, 2], [fundo_jogavel, 8, 3], [computador, 8, 4], [fundo_jogavel, 8, 5], [computador, 8, 6], [fundo_jogavel, 8, 7], [computador, 8, 8],
    [computador, 7, 1], [fundo_jogavel, 7, 2], [computador, 7, 3], [fundo_jogavel, 7, 4], [computador, 7, 5], [fundo_jogavel, 7, 6], [computador, 7, 7], [fundo_jogavel, 7, 8],
    [fundo_jogavel, 6, 1], [computador, 6, 2], [fundo_jogavel, 6, 3], [computador, 6, 4], [fundo_jogavel, 6, 5], [computador, 6, 6], [fundo_jogavel, 6, 7], [computador, 6, 8],
    [fundo_injogavel, 5, 1], [fundo_jogavel, 5, 2], [fundo_injogavel, 5, 3], [fundo_jogavel, 5, 4], [fundo_injogavel, 5, 5], [fundo_jogavel, 5, 6], [fundo_injogavel, 5, 7], [fundo_jogavel, 5, 8],
    [fundo_jogavel, 4, 1], [fundo_injogavel, 4, 2], [fundo_jogavel, 4, 3], [fundo_injogavel, 4, 4], [fundo_jogavel, 4, 5], [fundo_injogavel, 4, 6], [fundo_jogavel, 4, 7], [fundo_injogavel, 4, 8],
    [jogador, 3, 1], [fundo_jogavel, 3, 2], [jogador, 3, 3], [fundo_jogavel, 3, 4], [jogador, 3, 5], [fundo_jogavel, 3, 6], [jogador, 3, 7], [fundo_jogavel, 3, 8],
    [fundo_jogavel, 2, 1], [jogador, 2, 2], [fundo_jogavel, 2, 3], [jogador, 2, 4], [fundo_jogavel, 2, 5], [jogador, 2, 6], [fundo_jogavel, 2, 7], [jogador, 2, 8],
    [jogador, 1, 1], [fundo_jogavel, 1, 2], [jogador, 1, 3], [fundo_jogavel, 1, 4], [jogador, 1, 5], [fundo_jogavel, 1, 6], [jogador, 1, 7], [fundo_jogavel, 1, 8]]

posicao = 0
for c in tabuleiro:
    if posicao != c[1]:
        print()
    posicao = c[1]
    print(c[0], end='')
print('')
print('')

posicao = 0
while posicao == 0:
    posicao_x = int(input('x = '))
    posicao_y = int(input('y = '))
    for c in tabuleiro:
        if c[1] == posicao_x:
            if c[2] == posicao_y:
                if c[0] == 'o  ':
                    posicao = c[:]
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
print()

for c in tabuleiro:
    if c[1] == posicao_x:
        if c[2] == posicao_y:
            c[0] = 'o  '


for c in tabuleiro:
    if posicao != c[1]:
        print()
    posicao = c[1]
    print(c[0], end='')
print()

