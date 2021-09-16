import requests
from pyrogram import Client

from config import PrinceX
from helpers.filters import command


@Client.on_message(command(["asupan", f"asupan@{PrinceX.BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        await message.reply_text("Failed to get asupan from server...")
        print(ex)


@Client.on_message(command(["wibu", f"wibu@{PrinceX.BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        print(ex)
        await message.reply_text("Failed to get wibu from server...")


@Client.on_message(command(["chika", f"chika@{PrinceX.BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        print(ex)
        await message.reply_text("Failed to get chika from server...")


@Client.on_message(command(["truth", f"truth@{PrinceX.BOT_USERNAME}"]))
async def truth(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("Something went wrong...")


@Client.on_message(command(["dare", f"dare@{PrinceX.BOT_USERNAME}"]))
async def dare(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("Something went wrong...")


@Client.on_message(command(["lyric", f"lyric@{PrinceX.BOT_USERNAME}"]))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **Searching lyrics...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**Give a song name too !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception as ex:
        print(ex)
        await rep.edit("**Lyrics not found.** Please give a valid song name !")
