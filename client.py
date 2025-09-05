from websockets.asyncio.client import connect
from nicegui import ui
import asyncio
import ast
import datetime as dt
import random

messages_ = []
to_send = ""
user = ""

with ui.header():
    ui.label("Your-Chat")
    ui.input("username").bind_value(globals(), user)

async def get_messages():
    global messages_
    messages_ = []
    async with connect("ws://localhost:8765") as websocket:
        messages = await websocket.recv()
        messages_ = (ast.literal_eval(messages))

async def send():
    global to_send, user
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send(str({"body": to_send, "user": user, "stamp": f"{dt.datetime.now().hour}:{dt.datetime.now().minute}"}))

@ui.refreshable
def chat_display():
    global messages_
    for message in messages_:
        if message != "[]":
            if message["user"]:
                ui.chat_message(message["body"], name=message["user"], stamp=message["stamp"])
            else:
                ui.chat_message(message["body"], name="", stamp=message["stamp"])

async def loop():
    await get_messages()
    chat_display.refresh()

chat_display()
with ui.row():
    ui.input().bind_value(globals(), 'to_send')
    ui.button("send").on('click', lambda: send())

ui.timer(0.5, lambda: loop())

ui.run(dark=True)
