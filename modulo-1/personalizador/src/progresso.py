from rich.progress import Progress, SpinnerColumn
from rich.console import Console
import time

console = Console()

def print_progress_bar(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    with Progress() as progress:
        task = progress.add_task("[cyan]Processando...", total=100)
        for _ in range(100):
            progress.update(task, advance=1)
            time.sleep(0.01)
    console.print(content)

def print_progress_spinner(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    with Progress(SpinnerColumn()) as progress:
        task = progress.add_task("[green]Carregando...", total=None)
        time.sleep(1.5)  # Simula carregamento
    console.print(content)