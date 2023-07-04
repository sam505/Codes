import websockets
import asyncio


async def listen():
    url = "ws://127.0.0.1:8080"

    async with websockets.connect(url) as ws:
        while True:
            message = await ws.recv()
            print(message)


asyncio.get_event_loop().run_until_complete(listen())