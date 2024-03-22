import asyncio
import time


async def add1(x, y):
    print("startadd1")
    await asyncio.sleep(1)
    print("endadd1")
    return x + y

async def add2(x, y):
    await asyncio.sleep(2)
    return x + y

if __name__ == '__main__':
    asyncio.run(add1(2,3))
    print("over")
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(add1(1, 2))
    # end_time = time.time()
    # print(f"耗时{end_time - start_time}")
