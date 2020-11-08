import discord
from discord.ext import tasks, commands
import random
import ast
import os

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


client = commands.Bot(command_prefix='-')

muted = []


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('I am Ready'))


# hamu shtek jia akamawa la dwai har if statement'ek functionek bang akam
@client.command(aliases=["r", "revive", "un", "unmute"])
async def mute_or_unmute(ctx, player="everyone"):
    try:
        pp = player.split("!")[1].split(">")[0]
        mastername = client.get_user(int(pp))
    except:
        mastername = player
    try:
        vc = ctx.author.voice.channel
        for member in vc.members:
            if mastername == member or player == "everyone" and player not in muted:
                await member.edit(mute=False)
                await ctx.send(f"{member.name} has been unmuted. And was revived from death")
    except AttributeError:
        await ctx.send("You are not in a voice channel or that person is not on the same voice channel as you")




@client.command(aliases=["dead", "d", "mute", "m"])
async def mute_dead(ctx, player="everyone"):
    try:
        pp = player.split("!")[1].split(">")[0]
        mastername = client.get_user(int(pp))
    except:
        mastername = player

    if "KakAli" == mastername and ctx.author.name != "KakAli":
        await ctx.send("Who are you? to give your self the right of muting master!")
        return
    try:
        vc = ctx.author.voice.channel
        for member in vc.members:
            if mastername == member or player == "everyone" and player:
                muted.clear()
                await member.edit(mute=True)
                await ctx.send(f"{member.name} has been muted. And counted as dead for this round")
            if player != "everyone":
                muted.append(player)
    except AttributeError:
        await ctx.send("You are not in a voice channel or that person is not on the same voice channel as you")


@client.command(aliases=["question", "q"])
async def ask(ctx, *args):
    path = r"C:\Users\1234\Programming\python\Discord"
    with open(os.path.join(path, "src\\", "questions.txt")) as file:
        questions = [ast.literal_eval(line) for line in file]
        question = random.choice(range(205))
        await ctx.send(questions[0][question])


@client.command(aliases=["guess", "g"])
async def predict(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    if "arya" in question.lower():
        await ctx.send("You mare mortal is not worthy of talking about master!")
    else:
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command(aliases=["ping"])
async def show_ping(ctx):
    await ctx.send(f"ping: {round(client.latency * 1000)}ms")






@client.command(aliases=["p", "play"])
async def play_song(ctx):
    await ctx.send("this function is still under maintenance")





@client.command()
async def load(ctx, extension="all"):
    if extension == "all":
        for filename in os.listdir('./components'):
            if filename.endswith(".py"):
                client.load_extension(f"components.{filename.split('.')[0]}")
        await ctx.send("all the components were loaded")
    else:
        client.load_extension(f'components.{extension}')
        await ctx.send(f"{extension} was loaded")

@client.command()
async def unload(ctx, extension="all"):
    if extension == "all":
        for filename in os.listdir('./components'):
            if filename.endswith(".py"):
                client.unload_extension(f"components.{filename.split('.')[0]}")
        await ctx.send("all the components were unloaded")
    else:
        client.unload_extension(f'components.{extension}')
        await ctx.send(f"{extension} was unloaded")


@client.command()
async def reload(ctx, extension="all"):
    if extension == "all":
        for filename in os.listdir('./components'):
            if filename.endswith(".py"):
                client.unload_extension(f"components.{filename.split('.')[0]}")
                client.load_extension(f"components.{filename.split('.')[0]}")
        await ctx.send("all the components were reloaded")
    else:
        client.unload_extension(f'components.{extension}')
        client.load_extension(f'components.{extension}')
        await ctx.send(f"{extension} was reloaded")

try:
    for filename in os.listdir('./components'):
        if filename.endswith(".py"):
            client.load_extension(f"components.{filename.split('.')[0]}")
except Exception as e:
    pass





client.run('NzY2MjcxMzA5NzkzMzI5MjA1.X4g7xA.AvR7uMxgl79HSHeq4yozwx111Dk')
