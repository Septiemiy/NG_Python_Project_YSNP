import asyncio
import websockets
from adsBlocker_logical import makeJSONFromDict

async def server(websocket, path):
    try:
        html = await websocket.recv()
        makeJSONFromDict(html)
        await websocket.send('')
    except Exception as e:
        print(f"Error: {e}")

startServer = websockets.serve(server, "192.168.0.103", 8080, max_size=None)

print("Server start...")
asyncio.get_event_loop().run_until_complete(startServer)
asyncio.get_event_loop().run_forever()