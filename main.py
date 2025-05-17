from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import Responses

get_response = Responses().get_response

class BotError(Exception):
    pass

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
if TOKEN == None or TOKEN == '':
    raise BotError("Value DISCORD_TOKEN is empty in .env file.")
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        raise BotError("user_message was empty.")
    if is_private := (user_message[0] == "?" and user_message[1] == "p" and user_message[2] == " "):
        user_message = user_message[3:]
    response: str = get_response(user_message)
    if response != None:
        await message.author.send(response) if is_private else await message.channel.send(response)

@client.event
async def on_ready() -> None:
    print(client.user, 'is online.')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f"[{channel}] {username}: \"{user_message}\"")
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()
