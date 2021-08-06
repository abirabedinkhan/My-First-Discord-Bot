import discord
import requests

clinet = discord.Client()

@clinet.event
async def on_ready():
    print('Your Bot is ready as {0.user}'.format(clinet))

@clinet.event
async def on_message(message):
    if message.author == clinet.user:
        return

    msg = message.content
    sendMsg = message.channel.send

    if msg.startswith('$hello'):
        await sendMsg('Hello! {}'.format(message.author))

    if msg.startswith('$joke'):
        page = 'https://geek-jokes.sameerkumar.website/api'
        joke = getattr(requests.get(page), 'text', None)
        await sendMsg(joke.replace('"', ''))

if __name__ == '__main__':
    clinet.run('TOKEN')