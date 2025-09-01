import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20

    #container que mudará de cor (como uma caixa colorida)
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor!",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor = ft.Colors.GREY,
        width=300,
        height=100,
        border_radius=10,
        alignment=  ft.alignment.center
    )

    def cor_selecionada(evento):
        # Pegando qual cor foi selecionada
        cor_escolhida = evento.control.value

        cores_disponiveis = {
            "Azul": ft.Colors.BLUE,
            "Verde": ft.Colors.GREEN,
            "Vermelho": ft.Colors.RED,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Rosa": ft.Colors.PINK
        }

        # Mudando a cor da caixa
        caixa_colorida.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colorida.content.value = f"Cor selecionada: {cor_escolhida}"

        page.update()

    # Cirando a lista suspensa (dropdown)
    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa")
        ],
        on_change=cor_selecionada
    )

    page.add(
        ft.Text("Seletor de cores mágico!", size=24, weight=ft.FontWeight.BOLD),
        seletor_cor,
        caixa_colorida
    )

ft.app(target=main)