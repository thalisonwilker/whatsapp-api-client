# WhatsApp API Client

[Sobre a plataforma do WhatsApp Business](https://developers.facebook.com/docs/whatsapp/overview)

Cliente desenvolvido para interagir com a API oficial do WhatsApp

Preparação do ambiente

```sh
source venv/bin/activate
```

```sh
pip install -r requirements.txt
```

```sh
echo 'WHATSAPP_API_TOKEN=\nWHATSAPP_ACCOUNT_ID=' > .env
```

É importante preencher o .env com a chave de api e o id da conta whatsapp business

## Envio de Mensagens

#### Exemplo de envio de uma mensagem de texto simples (se o texto contiver uma URL o preview é adicionado automaticamente)
As mensagens de texto contêm apenas um corpo de texto e uma prévia de link opcional. Saiba mais em: [Sending Text Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/text-messages)


<center>
<img width="400" src="https://scontent.fbel17-1.fna.fbcdn.net/v/t39.2365-6/440742591_797870012016470_1123226266833971975_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=ryZnBQJFUusQ7kNvgHRO3xg&_nc_oc=AdigroSoBedZRJLcExARTyQgwvZ50IT9bgumzhr_kvj0UqRM0Mr2qiFlMQ1FFowpTpP59a_NAwNoHBjK5B_-XBx5&_nc_zt=14&_nc_ht=scontent.fbel17-1.fna&_nc_gid=AQ36FjgzsFLaA5VW51BLDa0&oh=00_AYDimpdvDKPXRlxkYXogeRdC33sP5F_q9ke71dbGgAn6ew&oe=67A3446B">
</center>

```py
from whatsapp import WhatsAppApi
from whatsapp.template_messages import Text

to = ""

message = Text(to, "Hello!")

api = WhatsAppApi()

api.send_message(message.payload)

```

#### Exemplo de envio de mensagens de lista interativas 
As mensagens de lista interativas permitem apresentar uma lista de opções para escolha dos usuários do WhatsApp. Saiba mais em: [Interactive List Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-list-messages)

<center>
<img width="400" src="https://scontent.fbel17-1.fna.fbcdn.net/v/t39.2365-6/439906651_815131396632137_2393939757123941379_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=XfzDT6LGtp0Q7kNvgGzvFKj&_nc_oc=AdgVA0b1_KWO6XM8KbULIF_6Ekl7QDyS6muZVWbv8B8nLA_L8YWzXpgsqXQebJlTDJdyWptLt9uiYR58wCMV_yd4&_nc_zt=14&_nc_ht=scontent.fbel17-1.fna&_nc_gid=A-QgiJ6D2IZbcdCxgR3bGPd&oh=00_AYBCj692f2XKpRo3IsAe04To6moJ8Gcmqv8Dl16NFpt_4w&oe=67A33AD1">
</center>

<center>
<img width="400" src="https://scontent.fbel17-1.fna.fbcdn.net/v/t39.2365-6/440772174_1215031642793437_4263879536705453309_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=40jRy32GSfUQ7kNvgFZljUl&_nc_oc=Adgbh3lW8qMT53_-o7fg-bnE6JUmlspQR0AXrQil3iMSkdjJ7dvGVf_MuK9I1a9SSPE7YnFJcKuhyymlYsf-H9Yk&_nc_zt=14&_nc_ht=scontent.fbel17-1.fna&_nc_gid=A-QgiJ6D2IZbcdCxgR3bGPd&oh=00_AYD5C6APFNls3MEDBXHitYlUNwai-Dhnfj5WUHJ5Egu0ug&oe=67A35C43">
</center>


```py
from whatsapp import WhatsAppApi
from whatsapp.template_messages import InteractiveList

to = ""

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
```

#### Exemplo de envio de mensagens com botões de resposta interativas 
As mensagens de botões de resposta interativas permitem que você envie até três respostas predefinidas para o usuário escolher. Saiba mais em: [Interactive Reply Buttons Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-reply-buttons-messages)

<center>
<img width="400" src="https://scontent.fbel17-1.fna.fbcdn.net/v/t39.2365-6/440749535_402938502645501_9105062754221017983_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=4KUCO4Nn0R4Q7kNvgEC05xd&_nc_oc=Adgt8PMbuBO47f2t2ef6a9gB0ZRzA0nWzvGy50M3k9NWcMbZM2aGR9QJDzHI5FFMCU2dZRDgTRzXGNCsDS45033U&_nc_zt=14&_nc_ht=scontent.fbel17-1.fna&_nc_gid=A33PXVzzHDmfoaNBjEVi3-K&oh=00_AYBNs3b6y9fpbdqjLl2vybrOx8rGicrq9UQ-opmq_D245w&oe=67A36931">
</center>

<center>
<img width="350" src="https://scontent.fbel17-1.fna.fbcdn.net/v/t39.2365-6/440803070_1108181003739406_7014741695346688945_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=qGkyX3qp9SkQ7kNvgFAA_oe&_nc_oc=AdjaSBWA2PuDGffm4n39bYKtFl37qmhlGWYd1ad_2OJ_Pe9_lQXZwLppcyHzxNoTvLQSLSkbhZGlQxeEkLzFU9MU&_nc_zt=14&_nc_ht=scontent.fbel17-1.fna&_nc_gid=A33PXVzzHDmfoaNBjEVi3-K&oh=00_AYD-leSDxG90LF9Aaw6Rzm151Y9G36FPVocA_bHoERdsMg&oe=67A33A86">
</center>

** Ainda sem suporte para envio de midias no header da mensagem.

```py
from whatsapp import WhatsAppApi
from whatsapp.template_messages import InteractiveList

to = ""

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
```

## Serializando os dados enviados ao Webhook

O Cliente possui uma interface que processa as mensagens enviada pela API ao webhook cadastrado na plataforma.
A interface tem como objetivo transformar o ```JSON``` recebido em um objeto **python** do tipo **MessageParser** que contém informações do tipo da mensagem recebida.


```py
from whatsapp.services.message_parser import MessageParser

parsed_message = MessageParser(data) # data: dados contidos no POST da requisição enviada ao webhook

if (parsed_message.message_type == "text"):
    ...
elif (parsed_message.message_type == "interactive.button_reply"):
    ...
elif (parsed_message.message_type == "interactive.list_reply"):
    ...

```

Para cada tipo de mensagem recebida o serializador contém dados específicos relaciodados ao objeto em questão e dados gerais relacioado ao paylod recebdio.

Todas as mensagens contem o **wamid**: WhastsApp Message ID, e **message_type**: tipo de mensagem recebida.

O **message_type** pode ser do tipo:
- **statuses**: atualização no status da mensagem
    - enviada, não enviada, entregue ou não entregue.
- **text**:
    - mensagem de texto
- **image**
    - a mensagem contém uma imagem
- **interactive**
    - mensagem interativa, pode ser uma lista interativa ou lista de botões interativa
- **interactive.button_reply**
    - resposta a uma mensagem com botões de resposta interativas

- **interactive.list_reply**
    - resposta a uma mensagem de lista interativas
