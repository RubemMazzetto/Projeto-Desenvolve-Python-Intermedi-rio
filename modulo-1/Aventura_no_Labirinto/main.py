import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar, solver_recursivo
from aventura_pkg.utils import imprime_instrucoes, imprime_menu, anima_vitoria_recursiva
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto.")
    parser.add_argument("--name", required=True, help="Nome do jogador (obrigatório).")
    parser.add_argument("--color", default="white", help="Cor principal (ex.: green).")
    parser.add_argument("--dificuldade", default="facil", choices=["facil", "dificil"], help="Dificuldade do labirinto.")
    parser.add_argument("--solver", action="store_true", help="Mostra solver recursivo.")
    args = parser.parse_args()

    console.print(f"Bem-vindo, {args.name}!", style="bold")
    labirinto = criar_labirinto(args.dificuldade)
    posicao, pontuacao = iniciar_jogador(labirinto)

    while True:
        escolha = imprime_menu()
        match escolha:
            case '1':
                imprime_instrucoes()
            case '2':
                def update():
                    console.clear()
                    imprimir_labirinto(labirinto, posicao, args.color)
                    console.print(pontuar(pontuacao))
                update()
                posicao, pontuacao = mover(labirinto, posicao, pontuacao, update)
                if labirinto[posicao[0]][posicao[1]] == 'E':
                    anima_vitoria_recursiva()
                    console.print("Vitória!")
                    break
            case '3':
                visitado = set()
                caminho = []
                solver_recursivo(labirinto, posicao, visitado, caminho)
                console.print(f"Solução: {caminho}")
            case '4':
                break
            case _:
                console.print("Opção inválida.")

if __name__ == "__main__":
    main()