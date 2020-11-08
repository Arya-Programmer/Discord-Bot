from discord.ext import commands
import asyncio

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, message, before, after):
        n = before.nick
        if after.nick not in ["arya", "4ry4", "ary4", "4rya"]:
            await message.channel.send("don't change your name to master, DESUU~")
        else:
            await message.channel.send(f"your nickname was changed from {before.nick} to {after.nick}")
            await after.edit(nick=f"{n}")

    @commands.Cog.listener()
    async def on_message(self, message):
        inner_check = message.author.name == "KakAli" and "asuna" in message.content.lower()
        if inner_check:
            await message.channel.send("Master... Did you call for me?")
        elif 'asuna' in message.content.lower():
            await message.channel.send("Yeah?")
        if inner_check or 'asuna' in message.content.lower():
            channel = message.channel
            def check(m):
                return m.content.lower() in ["yes", "yeah", "right", "em", "no"] and m.channel == channel

            try:
                msg = await self.bot.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                pass
            if str(msg.content).lower() in ["yeah", "yes", "right", "em"]:
                await message.channel.send("I am at your service master")
            else:
                await message.channel.send("sorry for bothering you")

def setup(bot):
    bot.add_cog(Events(bot))