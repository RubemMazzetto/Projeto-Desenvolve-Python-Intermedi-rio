from rich.console import Console
import time

console = Console()

def imprime_instrucoes() -> None:

    with open('instrucoes.txt', 'r') as f:
        console.print(f.read(), style="bold cyan")

def imprime_menu() -> str:

    console.print("1. Instruções\n2. Jogar\n3. Solver Recursivo\n4. Sair", style="bold yellow")
    return input("Escolha: ")

def anima_vitoria_recursiva(contador: int = 5) -> None:

    if contador == 0:
        return
    console.print(f"Vitória! {contador}", style="bold green")
    time.sleep(0.5)
    anima_vitoria_recursiva(contador - 1)