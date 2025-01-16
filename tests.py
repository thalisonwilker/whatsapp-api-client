from whatsapp import WhatsAppApi
from whatsapp.template_messages import Text

to = "5591981449182"

message = Text(to, "Hello!")

api = WhatsAppApi()

api.send_message(message.payload)