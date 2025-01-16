import json
import requests
from decouple import config

WHATSAPP_ACCOUNT_ID = config("WHATSAPP_ACCOUNT_ID")
WHATSAPP_API_TOKEN = config("WHATSAPP_API_TOKEN")

class WhatsAppApi:
    def __init__(self):
        self.API_KEY = WHATSAPP_API_TOKEN
        self.url = f'https://graph.facebook.com/v21.0/{WHATSAPP_ACCOUNT_ID}/messages'
        self.headers = {
            'authorization': f'Bearer {self.API_KEY}',
            "Content-Type": "application/json"}

    def send_message_reaction(self, to, message_id, emoji):
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "reaction",
            "reaction": {
                "message_id": message_id,
                "emoji": emoji
            }
        }
        requests.post(self.url, headers=self.headers, data=json.dumps(payload))

    def set_read_message(self, message_id):
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id
        }
        requests.post(self.url, headers=self.headers, data=json.dumps(payload))

    def send_message(self, payload):
        resp = requests.post(self.url, headers=self.headers,
                             data=json.dumps(payload))
        if(resp.status_code != 200):
            print(resp.status_code, "\n", resp.text)
