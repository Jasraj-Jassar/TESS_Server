# simple_ws_server.py
import asyncio
import websockets

connected_client = None

async def handler(websocket):
    global connected_client
    connected_client = websocket
    print("Client connected")
    
    try:
        async for message in websocket:
            # optional: print messages from client
            print(f"Received from client: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_client = None

async def input_loop():
    global connected_client
    while True:
        destination = await asyncio.to_thread(input, "Enter destination: ")

        if destination.strip() == "":
            print("Empty input, try again.")
            continue

        if connected_client is None:
            print("No client connected, cannot send.")
            continue

        try:
            await connected_client.send(destination)
            print(f"Sent destination: {destination}")
        except websockets.ConnectionClosed:
            print("Client disconnected while sending.")
            connected_client = None

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 7755)
    print("WebSocket server running on ws://0.0.0.0:7755")
    await asyncio.gather(server.wait_closed(), input_loop())

if __name__ == "__main__":
    asyncio.run(main())
