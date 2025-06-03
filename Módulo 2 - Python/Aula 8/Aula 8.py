import flet as ft

def man(page: ft.Page):
    def onclick(e):
        page.add(ft.Text(f"Seu nome é {nome_input.value}"))
        page.add(ft.Text(f"Seu nome é {idade_input.value}"))
    nome_input = ft.TextField(label="Nome:")
    idade_input = ft.TextField(label="Idade:")
    buttom = ft.ElevatedButton("Clique Aqui", on_click = onclick)
    page.add(buttom,nome_input,idade_input)
    ola = ft.Text(value="Olá mundo", size=50)
    page.controls.append(ola)
ft.app(target=man)

print ("hello world")
