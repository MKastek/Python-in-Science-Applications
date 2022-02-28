# asynchronicznie uruchomienie funkcji
# corutine - funkcja ktora mozemy uruchomic asynchronicznie
import asyncio

async def hello_asyn():
    await asyncio.sleep(5)
    print('Hello Async World!')

async def main():
    print('Im running')
    await hello_asyn()
    print('Im running')
    await hello_asyn()
    print('Im running')
    await hello_asyn()
    print('Im running')
    await hello_asyn()

asyncio.run(main())