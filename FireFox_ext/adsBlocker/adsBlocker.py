import asyncio
import websockets

async def server(websocket, path):
    data = await websocket.recv()
    print(f"Received data: {data}")
    # Тут ви можете обробити отримані дані від клієнта

start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()