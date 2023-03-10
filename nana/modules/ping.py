import time

from nana import app, Owner, Command
from pyrogram import Filters


@app.on_message(Filters.user(Owner) & Filters.command(["ping"], Command))
async def ping(client, message):
	start_time = time.time()
	await message.edit("š Pong!")
	end_time = time.time()
	ping_time = float(end_time - start_time)
	await message.edit("š Pong!\nā± Speed was : {0:.2f}s".format(round(ping_time, 2) % 60))
