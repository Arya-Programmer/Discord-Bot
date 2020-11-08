import discord
from discord.ext import commands
import datetime
from discord.embeds import Embed
import requests
from googleapiclient.discovery import build


class Search(commands.Cog):
    def __init__(self, bot):
        self.google = "https://rapidapi.p.rapidapi.com/api/v1/search/q={}&num={}"
        self.scopes = "https://www.googleapis.com/youtube/v3/search"
        self.headers = {
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "e7d5b07294msh9ba660adfc5ea3ep139be4jsne13b231a609d"
        }
        self.api_key = "AIzaSyBhsQ73opIFCks6hj7mc1f27zis45if41o"
        self.bot = bot

    @commands.command(aliases=['google'])
    @commands.Cog.listener()
    async def search_google(self, ctx, *, searchfor, resultNum=10):
        google = self.google.format(searchfor, resultNum).replace(" ", "+")
        realGoogle = "https://www.google.com/search?q={}"

        response = requests.request("GET", google, headers=self.headers)

        responseDict = eval(response.text)
        embed = Embed(title=f"```google search result for {searchfor}```",
                              colour=discord.Colour(0x4c51fc), url=f"{realGoogle.format(searchfor).replace(' ', '+') }",
                              description="[This]("+realGoogle.format(searchfor).replace(' ', '+') +") Is Top Ten Results To Your Search",
                              timestamp=datetime.datetime.utcnow())


        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/1004px-Google_%22G%22_Logo.svg.png")
        embed.set_author(name="Asuna-chan", icon_url="https://ih1.redbubble.net/image.254813860.9545/flat,750x1000,075,f.u2.jpg")
        embed.set_footer(text="Asuna Yuuki", icon_url="https://ih1.redbubble.net/image.254813860.9545/flat,750x1000,075,f.u2.jpg")

        for id, responses in enumerate(responseDict.get("results")):
            embed.add_field(name=f"search no.{id+1}", value=f"[`{responses.get('title')}`]({responses.get('link')})\n{responses.get('description')}", inline=False)
        await ctx.send(embed=embed)


    @commands.command(aliases=['youtube'])
    @commands.Cog.listener()
    async def search_youtube(self, ctx, *, searchFor):
        searchFor = searchFor.strip()
        count = 7
        if searchFor[-2::1].strip().isnumeric():
            count = searchFor[-2::1].strip()
            searchFor = searchFor[:-2].strip()

        youtube = build("youtube", 'v3', developerKey=self.api_key)
        youtubeUrl = "https://www.youtube.com/watch?v={}"

        params = {
            "part": 'snippet',
            "q": searchFor,
            "key": self.api_key,
            'max_results': count
        }
        r = requests.get(self.scopes, params=params)
        youtubeSearch = youtubeUrl.format(searchFor)
        embed = Embed(title=f"```youtube search result for {searchFor}```",
                      colour=discord.Colour(0x4c51fc), url=f"{youtubeSearch.replace(' ', '+')}",
                      description="[This](" + youtubeSearch.replace(' ', '+') + ") Is Top Ten Results To Your Search",
                      timestamp=datetime.datetime.utcnow())

        embed.set_thumbnail(url="https://i.pinimg.com/originals/de/1c/91/de1c91788be0d791135736995109272a.png")
        embed.set_author(name="Asuna-chan",
                         icon_url="https://ih1.redbubble.net/image.254813860.9545/flat,750x1000,075,f.u2.jpg")
        embed.set_footer(text="Asuna Yuuki",
                         icon_url="https://ih1.redbubble.net/image.254813860.9545/flat,750x1000,075,f.u2.jpg")

        for id, responses in enumerate(r.json().get('items')):
            if responses['id']['kind'] == 'youtube#video':
                youtubeSearch = youtubeUrl.format(responses['id']['videoId'])
                embed.add_field(name=f"search no.{id+1}",
                                value=f"[`{responses.get('snippet').get('title')}`]({youtubeSearch})\n{responses.get('snippet').get('description')}",
                                inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Search(client))
