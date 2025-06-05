#[PYIA-A10] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato.
#O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem.
#Após o usuário preencher esses campos, deve haver um botão de envio.
#Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.

import flet as ft

def main(page: ft.Page):

    # Campos do formulário
    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="Email", width=300)
    mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=4, width=300)

    # Texto de confirmação
    confirmacao = ft.Text(color="green")

    # Função chamada ao clicar no botão
    def enviar_formulario(e):
        if nome.value and email.value and mensagem.value:
            confirmacao.value = "Formulário enviado com sucesso!"
        else:
            confirmacao.value = "Por favor, preencha todos os campos."
            confirmacao.color = "red"
        page.update()

    # Botão de envio
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    # Adicionando todos os elementos à página
    page.add(
        ft.Column(
            controls=[
                ft.Text("Formulário de Contato", size=20, weight="bold"),
                nome,
                email,
                mensagem,
                botao_enviar,
                confirmacao
            ],
            spacing=15,
        )
    )

# Iniciar a aplicação
ft.app(target=main)
