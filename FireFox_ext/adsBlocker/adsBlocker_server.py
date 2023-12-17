import asyncio
import websockets

async def server(websocket, path):
    url = await websocket.recv()
    print(f"Received data: {url}")
    await websocket.send(url)

startServer = websockets.serve(server, "192.168.0.103", 8080)

asyncio.get_event_loop().run_until_complete(startServer)
asyncio.get_event_loop().run_forever()