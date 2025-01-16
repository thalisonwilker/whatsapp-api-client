# WhatsApp API Client

[Sobre a plataforma do WhatsApp Business](https://developers.facebook.com/docs/whatsapp/overview)

Cliente desenvolvido para interagir com a API oficial do WhatsApp

```sh
source venv/bin/activate
```

```sh
pip install -r requirements.txt
```

```sh
echo 'WHATSAPP_API_TOKEN=\nWHATSAPP_ACCOUNT_ID=' > .env
```

```py
from whatsapp import WhatsAppApi
from whatsapp.template_messages import Text

to = ""

message = Text(to, "Hello!")

api = WhatsAppApi()

api.send_message(message.payload)
```
