import asyncio

async def start():
    agent = "newbalance"
    module = __import__()

    return await module.crawl()

asyncio.get_event_loop().run_until_complete(start())