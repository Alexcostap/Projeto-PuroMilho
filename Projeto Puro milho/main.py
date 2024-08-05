import flet as ft
from models import *
def main(page: ft.Page):

    lista_produtos = ft.ListView()



    def inserir(conteudo):
        try:
            novo_produto = Produto(titulo=produto1.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(produto1.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=5,
                    #alignment = ft.Alignment.center
                    margin=5,
                    border_radius=15
                ))
            txt_erro.visible= False
            txt_acerto.visible = True
        except:
            txt_erro.visible= True
            txt_acerto.visible = False

            page.update(lista_produtos)
            print('Salvo')

    txt_erro = ft.Container(ft.Text('Erro ao salvar informação no banco de dados'), visible=False, bgcolor=ft.colors.RED_200, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Erro ao salvar informação no banco de dados'), visible=False, bgcolor=ft.colors.GREEN_400, alignment=ft.alignment.center)

    

    page.title = 'PURO MILHO'
    texto_titulo = ft.Text('Olá mundo!!', text_align=ft.TextAlign.LEFT) #Precisa adicionar ao page.add pois ele fica fora dessa função page
    produto1 = ft.TextField(label='Insira um nome do produto', text_align=ft.TextAlign.LEFT)
    texto_preco = ft.Text('Preço do Produto')
    preco = ft.TextField(label='Preço do produto',text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Inserir', on_click=inserir)

    
    largura = page.window.width = 300 #Largura da janela ao abrir
    altura = page.window.height = 700 #Altura da janela ao abrir
    page.add(
        txt_acerto,
        txt_erro,
        texto_titulo,
        produto1,
        texto_preco,
        preco,
        btn_produto
        
    )
    for x in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(x.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=5,
                #alignment=ft.alignment.center
                margin=5,
                border_radius=15
            )
        )
    page.add(
        lista_produtos
    )

ft.app(target=main)