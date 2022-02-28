# asynchronicznie uruchomienie funkcji
# corutine - funkcja ktora mozemy uruchomic asynchronicznie
import asyncio

async def hello_asyn():
    print('Hello Async World!')

async def main():
    print('Im running')
    await hello_asyn()
    await hello_asyn()
    await hello_asyn()
    await hello_asyn()

asyncio.run(main())