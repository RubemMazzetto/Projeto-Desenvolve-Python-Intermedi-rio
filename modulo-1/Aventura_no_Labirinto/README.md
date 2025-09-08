# Aventura no Labirinto

Jogo de exploração de labirinto via terminal. O jogador move-se com setas, coleta pontos e visa o exit. Usa recursão para solver, match-case no menu, rich para formatação, pynput para teclado, playsound para som.

## Configuração

1. Crie ambiente virtual: `python -m venv env`.
2. Ative: Windows `env\Scripts\activate`; Linux/Mac `source env/bin/activate`.
3. Instale dependências: `pip install -r requirements.txt`.
4. Rode: `python main.py --name SeuNome --dificuldade facil --color blue --disable-sound`.

## Como Jogar

- Menu: Escolha "instruções" ou "jogar".
- Movimentação: Setas (cima/baixo/esquerda/direita).
- Pontuação: +10 por movimento válido, -5 por parede.
- Vitória: Alcance 'E'. Use --solver para animação recursiva.

## Documentação

Abra `aventura_pkg.html` para docstrings.

## Clean Code

Funções pequenas, modulares, docstrings em tudo.