import os

import pyttsx3
from twitchio.ext import commands

from dotenv import load_dotenv
load_dotenv()


bot = commands.Bot(
    token=os.environ['TWITCH_TOKEN'],
    client_id=os.environ['TWITCH_CLIENT_ID'],
    nick=os.environ['TWITCH_NICK'],
    prefix='!',
    initial_channels=[os.environ['TWITCH_CHANNEL']]
)


@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')


@bot.command(name='say')
async def say(ctx, *, message: str):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', engine.getProperty('rate') - 50)
    engine.say(message)
    engine.runAndWait()

bot.run()
