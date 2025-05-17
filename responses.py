from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

class BotResponseError(Exception):
    pass
class Responses:
    def __init__(self):
        self.mute = False
        self.API_KEY = os.getenv("GCLOUD_API_KEY")
        if self.API_KEY == None or self.API_KEY == '':
            raise BotResponseError("Google Cloud API key in .env is empty.")
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.API_KEY}"
    def get_response(self, user_input: str) -> str:
        if user_input == "?mute" and self.mute == False:
            self.mute = True
            return "Ok! I will no longer respond. Unmute me with ?unmute."
        if user_input == "?unmute" and self.mute == True:
            self.mute = False
            return "I am no longer muted. Re-mute me with ?mute"
        if self.mute:
            return None
        payload: dict[str: list[dict[str: list[dict[str: str|int|None]]]]] = {"contents": [{"parts":[{"text": user_input}]}]}
        response = requests.post(self.url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            raise BotResponseError(f"Request failed with status code {response.status_code}: {response.text}")
