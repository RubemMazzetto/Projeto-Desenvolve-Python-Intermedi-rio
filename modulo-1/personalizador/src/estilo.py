from rich.text import Text
from rich.console import Console

console = Console()

def print_styled_bold(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    styled_text = Text(content, style="bold magenta")
    console.print(styled_text)

def print_styled_highlight(text: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(text, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        content = text

    styled_text = Text(content)
    styled_text.highlight_words(["python", "rich"], style="on yellow")
    console.print(styled_text)