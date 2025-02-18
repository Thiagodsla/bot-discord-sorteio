import discord
import random
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import typing

load_dotenv()
TK = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_message(message):
  await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f"Por favor, forneça um argumento. Exemplo: `/daily <nome_do_cargo>`.")
  else:
    raise error

@bot.command()
async def daily(ctx, args):
  membros = []
  for member in ctx.guild.members:
    if any(role.name.lower() == args.lower() for role in member.roles):
      if str(member.status) != 'offline' and str(member) != 'Bacon#9224':
        membros.append(member)

  random.shuffle(membros)
  if (len(membros)):
    await ctx.channel.send('Adivinha quem vai começar a daily hoje? 🥔 \nIsso mesmo, eu, **THE POTATOooooooooooooOOOo** !!! Minha tarefa foi sortear a ordem para a daily de hoje. 🥳 A ordem é essa aqui 👇    ')
  for user in membros:
    await ctx.channel.send(f'{user.mention}')

bot.run(TK)