import random
import discord
from discord.ext import commands
from youtube_search import YoutubeSearch
from translate import Translator
import asyncio
from art import *
import time

with open("token.txt", "r") as f:
    token = f.read().strip()


client = commands.Bot(command_prefix="!",  self_bot=True)


@client.event
async def on_ready():
    print("selfbot has woken up")
    print("                    _     _             _   ")
    print(" _ __    __ _   ___ | | __| |__    ___  | |_ ")
    print("| '_ \  / _` | / __|| |/ /| '_ \  / _ \ | __|")
    print("| |_) || (_| || (__ |   < | |_) || (_) || |_ ")
    print("| .__/  \__,_| \___||_|\_\|_.__/  \___/  \__|")
    print("|_|                                          ")
    time.sleep(2.5)
    print("welcome to packbot. yes. packbot")
    print("do you want to see features?")
    time.sleep(0.5)
    print("of course, you do. here are features")
    time.sleep(0.5)
    print("1. features: displays this list of available features.")
    print("2. ping: checks the bot's latency to the Discord servers and reports it.")
    print("3. clown: edits the previous message to include an image of a clown.")
    print("4. decrypt: funnu.  ")
    print("5. IP: another funnu. ")
    print("6. user_avatar: sends selected user's avatar.")
    print("7. rand: sends random number ( usage !rand min_num  max_num). ")
    print("8. !monkey : funnu monkey rap. ")
    print("9. !server_info : yk what it does. ")
    print("10. !clown : why am i writing this i made this command :skull: ")
    print("11. !searchvideo : searchs video on yt and sends link of it.")
    print(
        "12. !translate : translates text obviously. ( usage : !translate *original language* *language u want to translate to* *word* ). "
    )
    print(
        "13. !remindme : reminds u time or smth ( usage : !remindme 5m oven is burning) "
    )
    print("14. !random_memes : random memes video from youtube.")
    print("15. !play ")
    print("16. !watch ")
    print("17. !listen ")
    print("18. !stream ")
    print("19. !ascii : does text to ascii idk")


@client.command()
async def features(ctx):
    feature_list = "```Here are the available features and their descriptions:\n\n1. features: displays this list of available features.\n\n2. ping: checks the bot's latency to the Discord servers and reports it.\n\n3. clown: edits the previous message to include an image of a clown.\n\n4. decrypt: funnu.  \n\n5. IP: another funnu. \n\n6. user_avatar: sends selected user's avatar. \n\n7. rand: sends random number ( usage !rand min_num  max_num). \n\n8. !monkey : funnu monkey rap. \n\n9. !server_info : yk what it does. \n\n10. !clown : why am i writing this i made this command :skull: \n\n11. !searchvideo : searchs video on yt and sends link of it. \n\n12. !translate : translates text obviously. ( usage : !translate *original language* *language u want to translate to* *word* ). \n\n13. !remindme : reminds u time or smth ( usage : !remindme 5m oven is burning) \n\n14. !random_memes : random memes video from youtube. \n\n15. !play \n\n16. !watch \n\n17. !listen \n\n18. !stream \n\n19. !ascii : does text to ascii idk```"
    await ctx.send(feature_list)


@client.command()
async def ping(ctx):
    ping = round(client.latency * 1000)
    await ctx.send(f"Pong! {ping}ms")


@client.command()
async def rand(ctx, min: int, max: int):
    await ctx.send(random.randint(min, max))


@client.command()
async def ip(ctx, user: discord.Member):
    ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    message = f"{user.mention} ip =  ```{ip}```"
    await ctx.send(message)


@client.command()
async def user_avatar(ctx, user: discord.Member):
    await ctx.send(user.avatar_url)


@client.command()
async def decrypt(ctx, member: discord.Member):
    created_at = member.created_at.strftime("%A, %d %B %Y %I:%M %p")
    message = f"```                  [== Account Info ==]\n\n[Name: {member.display_name} | user id: {member.id}]\n\n{{Date Created: {created_at}}}``` \n ```Part of Token: MTA5NTI0ODIxMzgwNTYzNzY2Mw== | Base64 Encoded Stamp: MTY4MTIxMjMyMi4w | Bytes: b'MTY4MTIxMjMyMi4w' | Original TimeStamp: 1681212322.0, 2023-04-11 07:25:22.899000 |```"

    await ctx.send(message)


@client.event
async def on_message(message):
    if message.author == client.user and message.content.startswith("!monkey"):
        await message.edit(
            content="https://cdn.discordapp.com/attachments/1100047367559979079/1102534669423104030/rapidsave.com_five_litel_monks-mtttnxt5epy91.mp4"
        )
    if message.author == client.user and message.content.startswith("!clown"):
        await message.edit(
            content="https://cdn.discordapp.com/emojis/1073998192233943122.webp?size=96&quality=lossless"
        )

    await client.process_commands(message)


@client.command()
async def server_info(ctx):
    server = ctx.guild
    created_at = server.created_at.strftime("%A, %d %B %Y %I:%M %p")
    owner = server.owner if server.owner else "Not available"
    member_count = server.member_count
    roles_count = len(server.roles)

    message = f"**Server Information**\n\n"
    message += f"**Name: {server.name}**\n"
    message += f"**Created At: {created_at}**\n"
    if isinstance(owner, discord.Member):
        message += f"**Owner: {owner.mention}**\n"
    else:
        message += f"**Owner: {owner}**\n"
    message += f"**Member Count: {member_count}**\n"
    message += f"**Roles Count: {roles_count}**\n"

    await ctx.send(message)


@client.command()
async def searchvideo(ctx, search_text):
    results = YoutubeSearch(search_text, max_results=5).to_dict()

    if results:
        video = random.choice(results)
        video_url = f"https://www.youtube.com/watch?v={video['id']}"
        await ctx.send(video_url)
    else:
        await ctx.send("no videos found for the given search text.")


@client.command()
async def translate(ctx, source_lang, target_lang, *, text):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translated_text = translator.translate(text)

    translated_message = f"original text ({source_lang}): {text}\ntranslated text ({target_lang}): {translated_text}"
    await ctx.send(translated_message)


@client.command()
async def remindme(ctx, time, *, reminder):
    await ctx.send(
        f"sure i will xd, i will remind u in {time} with the message: {reminder}"
    )
    await asyncio.sleep(parse_time(time))
    await ctx.send(f"hey {ctx.author.mention}, you asked me to remind you: {reminder}")


@client.command()
async def disable_rpc(ctx):
    global enabled
    enabled = False
    await client.change_presence(activity=None)
    await ctx.send("RPC disabled.")


enabled = True


@client.command()
async def enable_rpc(ctx):
    global enabled
    enabled = True
    await ctx.send("RPC enabled.")


@client.command()
async def stream(ctx, name):
    if enabled:
        await client.change_presence(
            activity=discord.Streaming(
                name=name, url="https://www.twitch.tv/greengred_"
            )
        )
        await ctx.send(f"Streaming status set to '{name}'.")


@client.command()
async def listen(ctx, *, name):
    if enabled:
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name=name)
        )
        await ctx.send(f"Listening status set to '{name}'.")


@client.command()
async def watch(ctx, *, name):
    if enabled:
        activity = discord.Activity(type=discord.ActivityType.watching, name=name)
        await client.change_presence(activity=activity)
        await ctx.send(f"Now watching {name}")
    else:
        await ctx.send("RPC is disabled")


@client.command()
async def play(ctx, *, name):
    if enabled:
        await client.change_presence(activity=discord.Game(name=name))
        await ctx.send(f"Game status set to '{name}'.")


def parse_time(time_str):
    time_values = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    value = int(time_str[:-1])
    unit = time_str[-1]
    return value * time_values[unit]


@client.command()
async def random_memes(ctx):
    search_query = "discord memes"
    results = YoutubeSearch(search_query, max_results=10).to_dict()

    if results:
        video = random.choice(results)
        video_url = f"https://www.youtube.com/watch?v={video['id']}"
        await ctx.send(video_url)
    else:
        await ctx.send("No videos found.")

    print(video_url)

@client.command()
async def ascii(ctx, *, text):
    # Generating ASCII art
    ascii_text = text2art(text)

    # Sending the ASCII art as a message
    await ctx.send(f'```{ascii_text}```')



client.run(token)
