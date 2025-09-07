from rich.panel import Panel
from rich.console import Console

console = Console()

def print_panel_border(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    panel = Panel(content, title="Painel Estilizado", border_style="bold green")
    console.print(panel)

def print_panel_title(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    panel = Panel(content, title="Título Principal", subtitle="Subtítulo", border_style="blue")
    console.print(panel)