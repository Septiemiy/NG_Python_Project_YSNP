import asyncio
import websockets
from adsBlocker_logical import block_ads

async def server(websocket, path):
    url = await websocket.recv()
    #print(f"Received data: {html}")
    result = block_ads(url)
    await websocket.send(result)

startServer = websockets.serve(server, "192.168.0.103", 8080)

asyncio.get_event_loop().run_until_complete(startServer)
asyncio.get_event_loop().run_forever()