import discord
from discord.ext import commands
import random
import asyncio
import os
client = commands.Bot(command_prefix='q!')
@client.event
async def on_message(message):
  if(message.channel.id=="560913482933993477"):
    await client.add_reaction(message, ":check:561186041566855191")
    await client.add_reaction(message, ":x_cool:561185664679411722")

client.run('NTU5ODA3NjYyMjYzMzY5NzQ4.D3__Tg.lXfwyeLNorrb7OLkAkNfnpnxT9k')
