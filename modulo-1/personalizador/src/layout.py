from rich.layout import Layout
from rich.console import Console

console = Console()

def print_layout_split(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    layout = Layout()
    layout.split_column(
        Layout(content[:len(content)//2], name="Parte Superior"),
        Layout(content[len(content)//2:], name="Parte Inferior")
    )
    console.print(layout)

def print_layout_grid(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    layout = Layout()
    layout.split_row(
        Layout(content, name="Coluna 1"),
        Layout("Informação extra", name="Coluna 2")
    )
    console.print(layout)