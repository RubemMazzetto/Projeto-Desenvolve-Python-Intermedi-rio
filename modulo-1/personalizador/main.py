import argparse
from src import layout, painel, progresso, estilo

modulos = {
    '1': 'layout',
    '2': 'painel',
    '3': 'progresso',
    '4': 'estilo',
    'layout': 'layout',
    'painel': 'painel',
    'progresso': 'progresso',
    'estilo': 'estilo'
}

funcoes_por_modulo = {
    'layout': {
        '1': 'print_layout_split',
        '2': 'print_layout_grid',
        'print_layout_split': layout.print_layout_split,
        'print_layout_grid': layout.print_layout_grid
    },
    'painel': {
        '1': 'print_panel_border',
        '2': 'print_panel_title',
        'print_panel_border': painel.print_panel_border,
        'print_panel_title': painel.print_panel_title
    },
    'progresso': {
        '1': 'print_progress_bar',
        '2': 'print_progress_spinner',
        'print_progress_bar': progresso.print_progress_bar,
        'print_progress_spinner': progresso.print_progress_spinner
    },
    'estilo': {
        '1': 'print_styled_bold',
        '2': 'print_styled_highlight',
        'print_styled_bold': estilo.print_styled_bold,
        'print_styled_highlight': estilo.print_styled_highlight
    }
}

def main():
    parser = argparse.ArgumentParser(description="Formata texto ou conteúdo de arquivo usando o pacote personalizador com rich.")

    parser.add_argument("texto", type=str, help="Texto a ser formatado ou caminho para o arquivo de texto.")

    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento 'texto' é um caminho para arquivo.")

    parser.add_argument("-m", "--modulo", required=True, help="Módulo a ser usado (por nome ou ID): 1/layout, 2/painel, 3/progresso, 4/estilo.")

    parser.add_argument("-f", "--funcao", required=True, help="Função do módulo (por nome ou ID). Para layout: 1/print_layout_split, 2/print_layout_grid. Para painel: 1/print_panel_border, 2/print_panel_title. Para progresso: 1/print_progress_bar, 2/print_progress_spinner. Para estilo: 1/print_styled_bold, 2/print_styled_highlight.")

    args = parser.parse_args()

    modulo_key = args.modulo.lower()
    if modulo_key not in modulos:
        print("Módulo inválido. Opções: 1/layout, 2/painel, 3/progresso, 4/estilo.")
        return
    modulo_nome = modulos[modulo_key]

    funcao_key = args.funcao.lower()
    if funcao_key not in funcoes_por_modulo[modulo_nome]:
        print(f"Função inválida para {modulo_nome}. Consulte --help para opções.")
        return
    funcao = funcoes_por_modulo[modulo_nome][funcao_key]

    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()