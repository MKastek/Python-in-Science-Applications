# asynchronicznie uruchomienie funkcji
# corutine - funkcja ktora mozemy uruchomic asynchronicznie
# pobranie wyniku wykonania
import asyncio

async def hello_asyn():
    #pobranie informacji
    await asyncio.sleep(5)
    print('Hello Async World!')
    return 'return'

async def main():
    tasks = [asyncio.create_task(hello_asyn()) for _ in range(4)]
    for task in tasks:
        await task
    # await asyncio.gather(*tasks)

asyncio.run(main())