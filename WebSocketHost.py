import asyncio
import websockets

async def handle_connection(websocket):
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected.")
    except Exception as e:
        print("Error:", e)

async def main():
    try:
        async with websockets.serve(handle_connection, "0.0.0.0", 8080):
            print("WebSocket server running on ws://0.0.0.0:8080")
            await asyncio.Future()  # Run forever
    except Exception as e:
        print("Server error:", e)

if __name__ == "__main__":
    asyncio.run(main())
