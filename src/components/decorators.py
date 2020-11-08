import discord
from discord.ext import commands
import sqlite3


class decorations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['del', 'clear'])
    @commands.Cog.listener()
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} messages were deleted")

    @commands.command(aliases=['mention', 'men'])
    @commands.Cog.listener()
    async def mention_player(self, ctx, player: discord.User, amount=5):
        if amount < 50:
            for i in range(amount):
                await ctx.send(f"{player.mention}")

    @commands.command(pass_context=True, aliases=["k"])
    @commands.Cog.listener()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} was kicked!")

    @commands.command(aliases=['fuck'])
    @commands.Cog.listener()
    async def fuck_player(self, ctx, player):
        conn = sqlite3.connect('Words.sqlite')
        # making a cursor
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM BANNED")
        banned_words = cursor.fetchall()
        try:
            pp = player.split("!")[1].split(">")[0]
            mastername = self.bot.get_user(int(pp)).name
        except:
            try:
                pp = player.split("@")[1].split(">")[0]
                mastername = self.bot.get_user(int(pp)).name
            except:
                mastername = str('None')

        found = False
        for i in banned_words:
            if str(i[0].lower()) in player.lower() or i[0] in mastername and found == False:
                found = True
                await ctx.send("You mortal dare to disrespect master, are you seeking death(ban)?")
                break
        cursor.close()
        if found != True:
            if mastername != "None":
                await ctx.send(f"{mastername} is fucked.")
            else:
                await ctx.send(f"{player} is fucked.")

    @commands.command(aliases=['banw'])
    @commands.Cog.listener()
    async def ban_word(self, ctx, word):
        if ctx.author.name == "KakAli":
            conn = sqlite3.connect('Words.sqlite')
            cursor = conn.cursor()

            # sql_statement = '''CREATE TABLE BANNED(
            #     word text
            #     )'''
            #
            # cursor.execute(sql_statement)

            cursor.execute("""INSERT INTO BANNED VALUES (:word)""",{
                               'word': word,
                           })
            conn.commit()

            cursor.close()
            await ctx.send("done")

    @commands.command()
    @commands.Cog.listener()
    @commands.has_permissions(administrator=True)
    async def repeat(self, ctx, word, second=5, times=2):
        word = word.replace('-', ' ')
        for i in range(times):
            await ctx.send(f"{word}")
            # await sleep(second)




def setup(client):
    client.add_cog(decorations(client))
