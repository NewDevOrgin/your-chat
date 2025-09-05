import asyncio
import ast
import os
from websockets.asyncio.server import serve
from tinydb import TinyDB, Query

messages = TinyDB('messages.json')
PORT = int(os.environ.get("PORT", 8765))

async def chatG(websocket):
    global messages
    await websocket.send(str(messages.all()))

async def chatS(websocket):
    global messages
    async for message in websocket:
        print(f"1: {message}")
        message = ast.literal_eval(message)
        print(message)
        messages.insert({"body": message["body"], "stamp": message["stamp"]})

async def chat(websocket):
    await asyncio.gather(
        chatG(websocket),
        chatS(websocket)
    )

async def main():
    async with serve(chat, "localhost", PORT) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
