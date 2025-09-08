from random import randint
from rich.console import Console

console = Console()

def criar_labirinto(dificuldade: str) -> list:
    if dificuldade == 'facil':
        return [
            ['#', '#', '#', '#', '#'],
            ['S', ' ', ' ', ' ', '#'],
            ['#', '#', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', 'E'],
            ['#', '#', '#', '#', '#']
        ]
    else:
        # Mais complexo
        grid = [['#' for _ in range(7)] for _ in range(7)]
        # Gera caminhos aleatórios
        for i in range(1, 6):
            for j in range(1, 6):
                if randint(0, 1) == 0:
                    grid[i][j] = ' '
        grid[1][1] = 'S'
        grid[5][5] = 'E'
        return grid

def imprimir_labirinto(labirinto: list, posicao: tuple, color: str = 'white') -> None:
    lab_copy = [row[:] for row in labirinto]
    x, y = posicao
    lab_copy[x][y] = 'P'
    for row in lab_copy:
        console.print(' '.join([f'[{color}]{cell}[/{color}]' for cell in row]))