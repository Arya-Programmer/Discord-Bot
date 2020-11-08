import discord
from discord.ext import commands
from discord.utils import get
import discord

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

def setup(client):
    client.add_cog(Errors(client))