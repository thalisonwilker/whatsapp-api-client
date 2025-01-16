from whatsapp import WhatsAppApi
from whatsapp.template_messages import Text
from whatsapp.template_messages import InteractiveList
from whatsapp.template_messages import InteractiveReplyButtons

to = ""

message = Text(to, "Hello!")

api = WhatsAppApi()

api.send_message(message.payload)


actions = [
    {
        "id": "test-id-option-1",
        "title": "Opção 1",
        "description": "Essa é a descrição da opção 1"
    },
    {
        "id": "test-id-option-2",
        "title": "Opção 2",
        "description": "Essa é a descrição da opção 2"
    },
    {
        "id": "test-id-option-3",
        "title": "Opção 3",
        "description": "Essa é a descrição da opção 3"
    }
]

interative_list = InteractiveList(
    to=to,
    header_text="HEADER",
    body_text="Teste envio de listas interativa",
    footer_text="escolha com sabedoria uma das opções fonecidas",
    section_title="Escolha uma das opção",
    button_text="lista de opções",
    actions=actions
)

api.send_message(interative_list.payload)


buttons_options = [
    {
        "id": "button-option-1",
        "title": "SIM"
    },
    {
        "id": "button-option-2",
        "title": "NÃO"
    },
    {
        "id": "button-option-3",
        "title": "TALVEZ"
    }
]

interative_buttons_reply = InteractiveReplyButtons(
    to=to,
    header_text="Você gostaria de mais conhecimento ?",
    body_text="O conhecimento é essencial para o crescimento humano, expandindo horizontes, promovendo autonomia e permitindo melhores escolhas. Ele ilumina caminhos, transforma vidas e impulsiona a evolução pessoal e coletiva.",
    footer_text="E ai? o que vai ser ?",
    buttons=buttons_options
)

api.send_message(interative_buttons_reply.payload)