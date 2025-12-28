fundo_jogavel = '*  '
fundo_injogavel = '=  '
jogador = 'o  '
computador_ = 'x  '
azul = '\033[34m0  \033[0m'
magenta = '\033[35m1  \033[0m'
verde = '\033[32m2  \033[0m'
vermelho = '\033[31m3  \033[0m'
amarelo = '\033[33m4  \033[0m'
lista_magenta = []
todos = [azul, magenta, verde, vermelho, amarelo, computador_]
tabuleiro = [
    ['X   ', 9, 0],
    ['8  ', 8, 0], [fundo_injogavel, 8, 1], [computador_, 8, 2], [fundo_injogavel, 8, 3], [computador_, 8, 4], [fundo_injogavel, 8, 5], [computador_, 8, 6], [fundo_injogavel, 8, 7], [computador_, 8, 8],
    ['7  ', 7, 0], [computador_, 7, 1], [fundo_injogavel, 7, 2], [computador_, 7, 3], [fundo_injogavel, 7, 4], [computador_, 7, 5], [fundo_injogavel, 7, 6], [computador_, 7, 7], [fundo_injogavel, 7, 8],
    ['6  ', 6, 0], [fundo_injogavel, 6, 1], [computador_, 6, 2], [fundo_injogavel, 6, 3], [computador_, 6, 4], [fundo_injogavel, 6, 5], [computador_, 6, 6], [fundo_injogavel, 6, 7], [computador_, 6, 8],
    ['5  ', 5, 0], [fundo_jogavel, 5, 1], [fundo_injogavel, 5, 2], [fundo_jogavel, 5, 3], [fundo_injogavel, 5, 4], [fundo_jogavel, 5, 5], [fundo_injogavel, 5, 6], [fundo_jogavel, 5, 7], [fundo_injogavel, 5, 8],
    ['4  ', 4, 0], [fundo_injogavel, 4, 1], [fundo_jogavel, 4, 2], [fundo_injogavel, 4, 3], [fundo_jogavel, 4, 4],  [fundo_injogavel, 4, 5], [fundo_jogavel, 4, 6], [fundo_injogavel, 4, 7], [fundo_jogavel, 4, 8],
    ['3  ', 3, 0], [jogador, 3, 1], [fundo_injogavel, 3, 2], [jogador, 3, 3], [fundo_injogavel, 3, 4],  [jogador, 3, 5], [fundo_injogavel, 3, 6], [jogador, 3, 7], [fundo_injogavel, 3, 8],
    ['2  ', 2, 0], [fundo_injogavel, 2, 1], [jogador, 2, 2], [fundo_injogavel, 2, 3], [jogador, 2, 4], [fundo_injogavel, 2, 5], [jogador, 2, 6], [fundo_injogavel, 2, 7], [jogador, 2, 8],
    ['1  ', 1, 0], [jogador, 1, 1], [fundo_injogavel, 1, 2], [jogador, 1, 3], [fundo_injogavel, 1, 4], [jogador, 1, 5], [fundo_injogavel, 1, 6], [jogador, 1, 7], [fundo_injogavel, 1, 8],
    ['0  ', 0, 0], ['1  ', 0, 0], ['2  ', 0, 0], ['3  ', 0, 0], ['4  ', 0, 0], ['5  ', 0, 0], ['6  ', 0, 0],  ['7  ', 0, 0], ['8  ', 0, 0], ['Y  ', 0, 0], ]

from jogador import jogador_

jogador_()
