
class InteractiveReplyButtons:
    def __init__(self, to="", header_text="", body_text="", footer_text="", buttons=[]):
        """
            {
                "type": "reply",
                "reply": {
                    "id": "<BUTTON_ID>",
                    "title": "<BUTTON_LABEL_TEXT>"
                }
            }
        """

        buttons = [{ "type": "reply", "reply": { "id": b["id"], "title": b["title"] } } for b in buttons]

        self.payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "header": {
                    "type":"text",
                    "text": header_text,
                },
                "body": {
                    "text": body_text
                },
                "footer": {
                    "text": footer_text
                },
                "action": {
                    "buttons": buttons
                }
            }
        }
