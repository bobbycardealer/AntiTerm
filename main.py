from flask import Flask
from threading import Thread
import discord
import aiohttp
from discord.ext import commands

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)


Thread(target=run).start()


TOKEN = "YOUR_BOT_TOKEN" # <-- Place your Bot Token here  
CHANNEL_IDS = [xxxxx]  # Insert your Text Channel ID's here ( right click on Channel and then Copy Channeld ID ) :3

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.author.bot:
        return  

    if message.channel.id in CHANNEL_IDS:

        webhook = await message.channel.create_webhook(name=f"AntiTerm - {message.author.name}")


        files = [await attachment.to_file() for attachment in message.attachments]


        await webhook.send(
            content=message.content,
            username=message.author.name,
            avatar_url=message.author.avatar.url if message.author.avatar else None,
            files=files
        )

        await message.delete()
        await webhook.delete()

    await bot.process_commands(message)
bot.run(TOKEN)
