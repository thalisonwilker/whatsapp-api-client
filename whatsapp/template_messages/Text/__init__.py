
class Text:
    def __init__(self, to="", body="", preview_url=True):
        self.payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "text",
            "text": {
                "preview_url": preview_url,
                "body": body
            }
        }
