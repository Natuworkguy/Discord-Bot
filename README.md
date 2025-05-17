# 🧠 Customizable Discord Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-Natuworkguy-blueviolet)](https://github.com/Natuworkguy)

A simple, highly customizable Discord bot designed to give developers total control over response behavior through a single file: `responses.py`.

---

## ✨ Features

- 🧩 **Fully Customizable**: Tailor the bot's behavior by editing `responses.py`.
- ⚡ **Fast & Lightweight**: Minimal dependencies for quick deployment.
- 🧪 **Modular Design**: Easy to extend and maintain.
- 🔒 **.env Support**: Secure your token and sensitive configuration.

---

## 📁 Project Structure

```bash
dbot/
├── .env               # Store your Discord bot token here
├── banner.py          # Banner display on startup
├── main.py            # Main bot logic
├── responses.py       # Edit this file to define custom bot responses
├── requirements.txt   # Python package dependencies
└── startup.sh         # Shell script to launch the bot
````

---

## 🛠️ Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Natuworkguy/dbot.git
   cd dbot
   ```

2. **Create your `.env` file** (if not present):

   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Customize the bot**:

   Open `responses.py` and start customizing your bot’s response logic.

5. **Run the bot**:

   ```bash
   python main.py
   ```

   Or use the provided shell script:

   ```bash
   ./startup.sh
   ```

---

## 🧠 How to Customize

Open `responses.py`. This is where you define how your bot responds to different messages. You can define any number of conditions and customize replies however you want.

Default logic:

```python
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
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Maintainer

Made with ❤️ by [Natuworkguy](https://github.com/Natuworkguy)
