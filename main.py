import logging

logging.basicConfig(level=logging.INFO)

from pyrogram import Client, filters
from pyrogram.types import Message

m_api_id = 123456 # my.telegram.org/
m_api_hash = "1234dsfgdff5" # my.telegram.org/
m_chat_id = 123456

app = Client("bot", m_api_id, m_api_hash)

@app.on_message(filters.command(["help", "start"]))
async def start_help_commands(app, msg: Message):
	await msg.reply("To contact me, send a message here. Read @Nometaa before you send it \n\nIf you want an answer, put your id in the message")

@app.on_message(filters.forwarded)
async def forwarded(app, msg: Message):
	await msg.reply("You cannot forward someone else's messages")

@app.on_message()
async def send_message(app, msg: Message):
	await app.copy_message(m_chat_id, msg.from_user.id, msg.id)
	await msg.reply("Message send")

app.run()