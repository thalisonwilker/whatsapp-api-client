
class MessageParser:
    def __init__(self, data):
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        statuses = value.get("statuses", False)
        messages = value.get("messages", False)

        if(statuses):
            self.message_type = "statuses"
            statuses = statuses[0]
            self.wamid = statuses["id"]
            self.status = statuses["status"]

        if(messages):
            messages = messages[0]

            self.message_type = messages["type"]
            self.from_number = messages["from"]
            self.wamid = messages["id"]

            if(self.message_type == "text"):
                text = messages["text"]
                self.message_text = text["body"]

                contacts = value["contacts"][0]
                profile = contacts["profile"]
                self.wa_id = contacts["wa_id"]
                self.profile_name = profile["name"]

            elif(self.message_type == "image"):
                image = messages["image"]
                caption = image.get("caption", "")
                media_id = image["id"]

            elif(self.message_type == "interactive"):
                interactive = messages["interactive"]

                interactive_type = interactive["type"]

                if(interactive_type == "button_reply"):
                    self.message_type = "interactive.button_reply"
                    button_reply = interactive["button_reply"]
                    self.button_reply_id = button_reply["id"]
                    self.button_reply_title = button_reply["title"]
                elif(interactive_type == "list_reply"):
                    self.message_type = "interactive.list_reply"
                    list_reply = interactive["list_reply"]
                    self.list_reply_id = list_reply["id"]
                    self.list_reply_title = list_reply["title"]
                    self.list_reply_description = list_reply["description"]