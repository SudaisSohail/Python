import asyncio

async def Main():
    print("Ibrahim")
    task = asyncio.create_task(foo("text"))
    await task
    print("Finished")

async def foo(text):
    print(text)
    await asyncio.sleep(1) 


asyncio.run(Main())

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    print("Done fetching")
    return {"Data" : 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)
    await task2


asyncio.run(main())