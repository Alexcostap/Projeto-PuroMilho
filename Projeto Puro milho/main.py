import flet as ft
from models import *
def main(page: ft.page):

    lista_produtos = ft.ListView()



    def inserir(conteudo):
        novo_produto = Produto(titulo=produto1.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()
        print('Salvo')




    page.title = 'PURO MILHO'
    texto_titulo = ft.Text('Olá mundo!!', text_align=ft.TextAlign.LEFT) #Precisa adicionar ao page.add pois ele fica fora dessa função page
    produto1 = ft.TextField(label='Insira um nome do produto', text_align=ft.TextAlign.LEFT)
    texto_preco = ft.Text('Preço do Produto')
    preco = ft.TextField(label='Preço do produto',text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Inserir', on_click=inserir)

    for x in session.query(Produto).all():
        print(x)
    largura = page.window.width = 300 #Largura da janela ao abrir
    altura = page.window.height = 500 #Altura da janela ao abrir
    page.add(
        texto_titulo,
        produto1,
        texto_preco,
        preco,
        btn_produto
    )

    
ft.app(target=main)