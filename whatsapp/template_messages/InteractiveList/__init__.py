

class InteractiveList:
    def __init__(self, to="", header_text="", body_text="", footer_text='', section_title="", button_text="", actions=[]):
        """
            {
                "id": "<ROW_ID>",
                "title": "<ROW_TITLE_TEXT>",
                "description": "<ROW_DESCRIPTION_TEXT>"
            }
        """
        self.payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": header_text
                },
                "body": {
                    "text": body_text
                },
                "footer": {
                    "text": footer_text
                },
                "action": {
                    "sections": [
                        {
                            "title": section_title,
                            "rows": actions
                        }
                    ],
                    "button": button_text,
                }
            }
        }
