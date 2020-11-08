import discord
from discord.ext import commands
import asyncio
import speech_recognition as sr




class Example(commands.Cog):
    def __init__(self, client):
        self.bot = client

    # @commands.Cog.listener()
    # def play(self, ctx):
    #     author = ctx.message.author
    #     channel = author.voice_channel
    #     await self.bot.join_voice_channel(channel)
    #     vc = await channel.connect()
    #     print(vc.listen())
        # mic_name = "Microphone (High Definition Audio Device)"
        # sample_rate = 48000
        # chunk_size = 2048
        # r = sr.Recognizer()
        #
        # mic_list = sr.Microphone.list_microphone_names()
        # for j,k in enumerate(mic_list):
        #     print(j, ".", k)
        #
        # with sr.Microphone(device_index=0, sample_rate=sample_rate, chunk_size=chunk_size) as source:
        #     r.adjust_for_ambient_noise(source)
        #     print("Say Something")
        #     audio = r.listen(source)
        #
        #     try:
        #         global text
        #         text = r.recognize_google(audio)
        #         print("you said: " + text)
        #         # error occurs when google could not understand what was said
        #     except sr.UnknownValueError:
        #         print("Google Speech Recognition could not understand audio")
        #     except sr.RequestError as e:
        #         print("Could not request results from Google Speech Recognitionn service; {0}".format(e))


def setup(client):
    client.add_cog(Example(client))