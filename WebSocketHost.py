import asyncio
import websockets

async def echo(websocket, path):
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")

async def main():
    server = await websockets.serve(echo, "0.0.0.0", 5555)
    print("WebSocket server running on ws://0.0.0.0:5555")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
