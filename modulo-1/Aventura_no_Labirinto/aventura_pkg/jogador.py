from pynput import keyboard
from rich.console import Console
import time

console = Console()

def iniciar_jogador(labirinto: list) -> tuple:

    for i, row in enumerate(labirinto):
        if 'S' in row:
            return (i, row.index('S')), 0
    return (0, 0), 0

def mover(labirinto: list, posicao: tuple, pontuacao: int, callback: callable) -> tuple:
    def on_press(key):
        nonlocal posicao, pontuacao
        dx, dy = 0, 0
        if key == keyboard.Key.up: dx = -1
        elif key == keyboard.Key.down: dx = 1
        elif key == keyboard.Key.left: dy = -1
        elif key == keyboard.Key.right: dy = 1
        new_x, new_y = posicao[0] + dx, posicao[1] + dy
        if 0 <= new_x < len(labirinto) and 0 <= new_y < len(labirinto[0]) and labirinto[new_x][new_y] != '#':
            posicao = (new_x, new_y)
            pontuacao += 10
        else:
            pontuacao -= 5
        callback()
        if labirinto[new_x][new_y] == 'E':
            return keyboard.Listener.StopListening

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    return posicao, pontuacao

def pontuar(pontuacao: int) -> str:

    return f"Pontuação: {pontuacao}"

def solver_recursivo(labirinto: list, posicao: tuple, visitado: set, caminho: list) -> bool:

    x, y = posicao
    if labirinto[x][y] == 'E':
        return True
    visitado.add(posicao)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(labirinto) and 0 <= new_y < len(labirinto[0]) and labirinto[new_x][new_y] != '#' and (new_x, new_y) not in visitado:
            caminho.append((dx, dy))
            if solver_recursivo(labirinto, (new_x, new_y), visitado, caminho):
                return True
            caminho.pop()
    return False