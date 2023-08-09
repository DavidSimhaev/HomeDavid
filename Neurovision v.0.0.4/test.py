import asyncio
import threading

async def my_coroutine():
    print("Hello, World!")

def run_coroutine_threadsafe(loop):
    asyncio.run_coroutine_threadsafe(my_coroutine(), loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    thread_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(thread_loop)

    thread = threading.Thread(target=run_coroutine_threadsafe, args=(loop,))
    thread.start()

    asyncio.run_forever()