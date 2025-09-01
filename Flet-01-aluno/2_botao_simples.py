import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro botão"
    page.padding = 20

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo!",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):

        # Mudando o texto da mensagem
        mensagem.value = "Parabéns! Você clicou no botão!"
        mensagem.color = ft.Colors.GREEN
        # IMPORTANTE: Sempre que modificar elementos da interface,
        # precisamos chamar page.update() para que as mudanças aparecam na tela

        page.update()
    
    # Criando nosso botão
    botao = ft.ElevatedButton(
        text="Clique em mim!", # Texto do botão
        on_click=botao_clicado, # Função que será executada no clique
        width=200, # Largura
        height=50, # Altura
        bgcolor=ft.Colors.BLUE, # Cor de fundo
        color=ft.Colors.WHITE # Cor do texto
    )

    # Adicionando o elementos à página
    page.add(mensagem)
    page.add(botao)

ft.app(target=main)