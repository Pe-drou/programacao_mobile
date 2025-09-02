import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Loja Virtual Mini"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO # Permite a rolagem automática da página
    page.hgcolor = ft.Colors.GREY_50 # Cor de fundo da página

    # Estado da aplicação - Variáveis que armazenam dados do carrinho
    carrinho = [] # Lista que armazena os produtos do carrinho
    total_carrinho = 0.0 # Valor total dos produtos do carrinho

    # Elementos da interface (declarados primeiro para serem acessíveis nas funções)
    
    # Grid que exibe os produtos em formato de grade
    area_produtos = ft.GridView(
        expand=1,               # Expande para ocupar espaço disponível
        runs_count=2,           # 2 colunas de produtos
        max_extent=180,         # Largura máxima de cada item
        child_aspect_ratio=0.9, # Proporção altura/largura dos cards
        spacing=15,             # Espaçamento entre cards horizontalmente
        run_spacing=15          # Espaçamento entre cards verticalmente
    )

    # Textos que mostram informações do carrinho
    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)

    # Lista que exibe os itens do carrinho
    lista_carrinho = ft.ListView(height=150, spacing=5)

    # Texto para exibir notificações ao usuário
    notificacao = ft.Text("", size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    def adicionar_ao_carrinho(nome, preco):
        nonlocal total_carrinho # Permite modificar a variável global total_carrinho

        # Adiciona o produto como dicionário na lista do carrinho
        carrinho.append({"nome": nome, "preco": preco})
        # Soma o preço dos produtos ao total
        total_carrinho += preco
        # Atualiza a interface do carrinho
        atualizar_carrinho()
        # Mostra nofiticação de sucesso
        mostrar_notificacao(f"{nome} adicionado ao carrinho!")
    
    def criar_card_produto(nome, preco, categoria, emoji, cor):
        return ft.Container(
            content=ft.Column([
                # Emoji do produto
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                # Nome do produto
                ft.Text(nome, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER,
                        max_lines=2, #permite quebra de linha para nnomes longo
                        overflow=ft.TextOverflow.ELLIPSIS # Adiciona "..." se muito longo
                        ),
                # Preço do produto
                ft.Text(f"R$ {preco:.2f}", size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            bgcolor=cor, # Cor de fundo específica do produto
            padding=20, border_radius=15, width=160, height=180,
            shadow=ft.BoxShadow( #Sombra para dar profundidade
                spread_radius=1, blur_radius=8, color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            ),
            # Tornando o card inteiro clicável - chama função de adicionar ao carrinho
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n,p),
            # Efeito visual de ondulação ao clicar (ripple effect)
            ink=True
        )
    
    # Lista de produtos disponíveis na loja

    # Cada produto é um dicionário com informações como nome, preço, categoria, emoji e cor
    produtos = [
        {
            "nome": "Smartphone",
            "preco": 899.99,
            "categoria": "Eletrônicos",
            "emoji": "📱",
            "cor": ft.Colors.BLUE_600
        },
        {
            "nome": "Notebook",
            "preco": 2499.99,
            "categoria": "Eletrônicos",
            "emoji": "💻",
            "cor": ft.Colors.PURPLE_600
        },
        {
            "nome": "Tênis",
            "preco": 299.99,
            "categoria": "Roupas",
            "emoji": "👟",
            "cor": ft.Colors.GREEN_600
        },
        {
            "nome": "Camiseta",
            "preco": 89.99,
            "categoria": "Roupas",
            "emoji": "👕",
            "cor": ft.Colors.ORANGE_600
        },
        {
            "nome": "Livro",
            "preco": 49.99,
            "categoria": "Educação",
            "emoji": "📕",
            "cor": ft.Colors.BROWN_600
        },
        {
            "nome": "Fone",
            "preco": 199.99,
            "categoria": "Eletrônicos",
            "emoji": "🎧",
            "cor": ft.Colors.RED_600
        },
        {
            "nome": "Relógio",
            "preco": 359.99,
            "categoria": "Acessórios",
            "emoji": "⌚",
            "cor": ft.Colors.TEAL_600
        },
        {
            "nome": "Óculos de Sol",
            "preco": 249.99,
            "categoria": "Acessórios",
            "emoji": "🕶️",
            "cor": ft.Colors.INDIGO_600
        }

# ~~~~~ TEMPLATE DE CRIAÇÃO DE PRODUTOS ~~~~~
        # {
        #     "nome": "",
        #     "preco": 0.0,
        #     "categoria": "",
        #     "emoji": "",
        #     "cor": ft.Colors.GREY
        # },
    ]

    # Elementos de filtro da interface
    # Dropdown para filtros por categoria
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        width=150,
        value="Todas", # Valor padrão
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Eletrônicos"),
            ft.dropdown.Option("Roupas"),
            ft.dropdown.Option("Educação"),
            ft.dropdown.Option("Acessórios")
        ]
    )

    # Dropdown para filtrar por faixas de preço
    filtro_preco = ft.Dropdown(
        label="Preço",
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Até R$ 100"),
            ft.dropdown.Option("R$ 100-500"),
            ft.dropdown.Option("Acima de R$ 500")
        ]
    )

    # campo de texto para buscar produtos por nome
    campo_busca = ft.TextField(
        label="Buscar Produto",
        width=200,
        prefix_icon=ft.Icons.SEARCH
    )

    def remover_do_carrinho(index):
        nonlocal total_carrinho # Permite modificar a variável global total_carrinho
        # Verificar se o indice é valido (existe na lista)
        if 0<= index < len(carrinho):
            # Remove o produto da lista e armazena os dados dele
            produto = carrinho.pop(index)
            # Subtrai o preco do produto do total
            total_carrinho -= produto["preco"]
            # atualiza a interface do carrinho
            atualizar_carrinho()
            # mostra a notificação de remoção
            mostrar_notificacao(f"{produto['nome']} removido do carrinho!")
    
    def atualizar_carrinho():
        #atualiza o contador de itens no carrinho
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        # atualiza o valor total formatado em reais
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"
        # limpa a lista visual do carrinho
        lista_carrinho.controls.clear()

        # adiciona cada item do carrinho na lista visual
        for i, item in enumerate(carrinho):
            # cria uma linha para cada produto no carrinho
            linha_produto = ft.Row([
                # nome do produto (expande para ocupar espaço disponível)
                ft.Text(f"{item['nome']}", expand=True),
                # preço do produto (expande para ocupar espaço disponível)
                ft.Text(f"R$ {item['preco']:.2f}", color=ft.Colors.GREEN_600),
                # botão para remover o produto (usando o índice atual)
                ft.IconButton(
                    ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e, idx=i: remover_do_carrinho(idx)
                )
            ], spacing=10)

            # adiciona a lista à lista visual
            lista_carrinho.controls.append(linha_produto)
        
        # atualiza a página para refletir as mudanças
        page.update()
    
    def carregar_produtos(e=None):
        # limpar a área de produtos antes de recarregar
        area_produtos.controls.clear()

        # obtém os valores dos filtros
        categoria = filtro_categoria.value
        preco_faixa = filtro_preco.value
        busca = (campo_busca.value or "").lower() # lower() converte para minúscula para buscar

        # percorre todos os produtos disponíveis
        for produto in produtos:
            # aplica filtro de categoria
            if categoria != "Todas" and produto["categoria"] != categoria:
                continue # pula esse produto se não bater com a categoria
                
            # aplica fultro de preço
            if preco_faixa == "Até R$ 100" and produto["preco"] > 100:
                continue
            elif preco_faixa == "R$ 100-500" and not (100 <= produto["preco"] <= 500):
                continue
            elif preco_faixa == "Acima de R$ 500" and produto["preco"] <= 500:
                continue
        
            # aplica filtros de busca por nome
            if busca and busca not in produto["nome"].lower():
                continue

            # se chegoul até aqui, o produto passou por todos os filtros
            # criar o card do produto
            card = criar_card_produto(
                produto["nome"],
                produto["preco"],
                produto["categoria"],
                produto["emoji"],
                produto["cor"]
            )

            # Adicionao card à área de produtos
            area_produtos.controls.append(card)
        
        # atualiza a página para mostrar os produtos filtrados
        page.update()

    def finalizar_compra(e):
        nonlocal total_carrinho
        if len(carrinho) > 0:
            #limpar completamente a lista de carrinho
            carrinho.clear()
            #zera o total (importante: usar nonlocal para modificar a variavel global)
            total_carrinho = 0.0
            #atualiza a interface do carrinho
            atualizar_carrinho()
            #mostrsa a mensagem de sucesso
            mostrar_notificacao(f"Compra finalizada! Obrigado(a)!")
        else:
            #mostra mensagem de sucesso
            mostrar_notificacao("Carrinho vazio! Que tal adicionar alguns produtos?")
    
    def limpar_filtros(e):
        # redefine todos os filtros para seus valores iniciais
        filtro_categoria.value="Todas"
        filtro_preco.value="Todos"
        campo_busca.value=""
        #recarrega os produtos sem filtros
        carregar_produtos()
        #mostra a notificação de que os filtros foram limpos
        mostrar_notificacao("Filtros limpados!")

    def mostrar_notificacao(mensagem):
        notificacao.value = mensagem
        page.update()
    
    #conecta os eventos de mudança dos filtros à função de carregar produtos
    #sempre que o usuário mudar algum filtro, os produtos seráo recarregados
    for controle in [filtro_categoria, filtro_preco, campo_busca]:
        controle.on_change = carregar_produtos
    
    #carrega os produtos inicialmente (sem filtros)
    carregar_produtos()

    # construção da interface do usuário
    page.add(
        ft.Column([
            # cabeçalho da loja
            ft.Text(
                "Loja Virtual Mini",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Encontre os melhores produtos!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            ),

            # Seção de filtros
            # Filtros de categoria e preço
            ft.Row(
                [filtro_categoria, filtro_preco],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            # Campo de busca e botão limpar filtros
            ft.Row([
                campo_busca,
                ft.ElevatedButton(
                    "Limpar filtros",
                    on_click=limpar_filtros,
                    bgcolor=ft.Colors.ORANGE_400,
                    color=ft.Colors.WHITE,
                    height=40,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)
                    )
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),

            # área principal onde os produtos são exibidos
            ft.Container(
                content=area_produtos,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10
            ),

            # seção do carrinho de compras
            ft.Container(
                content=ft.Column([
                    # linha com contador de itens e total
                    ft.Row(
                        [contador_carrinho, total_texto],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    # lista os itens no carrinho
                    lista_carrinho,
                    # botão para finalizar compra
                    ft.Row([
                        ft.ElevatedButton(
                            "Finalizar compra",
                            on_click=finalizar_compra,
                            bgcolor=ft.Colors.GREEN,
                            color=ft.Colors.WHITE,
                            width=200
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    notificacao
                ], spacing=10),
                bgcolor=ft.Colors.WHITE,
                padding=20,
                border_radius=10,
                # sombra sutil para destacar o carrinho
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=3,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                )
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
    )

ft.app(target=main)


