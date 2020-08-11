import discord
from discord.ext import commands
import json

f = open('newsletters.json', 'w')

bot = commands.Bot(command_prefix=',')
token = list(open('token.txt'))[0]


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def create(ctx, *, name):
    data = {
        'Name': name,
        'User ID': ctx.author.id
    }
    json.dump(data, f)


bot.run(token)
