# Habilita o uso do flet no 
import flet as ft

# Abre a página "main" 
def main(page: ft.Page):
    # Variável para um Input de texto
    txt_name = ft.TextField(label="Seu Nome")
    # Vetor de botão
    def btn_click(e):
        # Função de adicionar uma mensagem quando o botão for pressionado
        page.add(ft.Text(f'Olá, {txt_name.value}!'))
    # Função para adiconar os elementos à pagina
    page.add(txt_name, ft.ElevatedButton("Dizer olá", on_click=btn_click))
# Função para visualizar o site
ft.app(target=main)