import asyncio
import websockets
from adsBlocker_logical import block_ads

async def server(websocket, path):
    html = await websocket.recv()
    print(html)


startServer = websockets.serve(server, "192.168.0.103", 8080, max_size=None)

asyncio.get_event_loop().run_until_complete(startServer)
asyncio.get_event_loop().run_forever()