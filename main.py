import discord
from discord.ext import commands

def main():
intents = discord.Intents().all()
client = commands.Bot(command_prefix='u!', intents=intents)
client.remove_command('info')

@client.event
async def on_ready():
    print("Unicorny на месте...")

@client.command()
async def tank(ctx):
    await ctx.send("https://i.pinimg.com/originals/88/80/72/8880722f932c12f4a93ce18c389af130.jpg")

client.run("MTAxNzg5MTE0ODUzNjIzODE0MA.G6RrRl.YoD1N5kj9e5YcHYgJoB546IBlV4W0WfwTls1NY")

if __main__ = '__main__':
    main()
