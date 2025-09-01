# Primeiro programa desenvolvido em phyton
import flet as ft

def main(page: ft.Page):
    
    # Confiurações da página
    page.title = "Meu Primeiro App Flet" # Titulo que aparece na aba do navegador
    page.padding = 20 # Espaçamento interno da página

    # Criando o primeiro elemento: um texto
    texto = ft.Text(
        value="Hello world!", # O texto que será exibido
        size=24, # Tamanho da fonte
        color=ft.Colors.BLUE, # Cor do texto
        weight=ft.FontWeight.BOLD, # Texto em negrito (bold)
        text_align=ft.TextAlign.CENTER # Centraliza o texto
    )

    # Adicionando o texto à página
    page.add(texto)

    # Adicionar mais elementos para ficar mais interessante
    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=16),
        ft.Text("Com Flet, você pode criar apps incríveis!", size=16, color=ft.Colors.GREEN)
    )
    

# Esta linha iniciará o aplicativo, chamando a função main
ft.app(target=main)