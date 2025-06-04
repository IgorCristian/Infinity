#[PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. 
#A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. 
#Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento.
#A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.

import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    

    # Campo de entrada para a tarefa
    input_tarefa = ft.TextField(label="Digite a tarefa", expand=True)

    # Lista que armazenará os itens de tarefa
    lista_tarefas = ft.Column()

    # Função chamada ao clicar no botão
    def adicionar_tarefa(e):
        if input_tarefa.value.strip() != "":
            lista_tarefas.controls.append(ft.Text(f"• {input_tarefa.value}"))
            input_tarefa.value = ""
            page.update()

    # Botão de adicionar
    botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)

    # Monta a interface
    page.add(
        ft.Row([input_tarefa, botao_adicionar]),
        lista_tarefas
    )

# Executa o app
ft.app(target=main)