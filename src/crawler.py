import asyncio
import json

async def start():
    f = open('./input.json')
    products = json.load(f)
    shoes = products['list']
    for shoe in shoes:
        module = __import__(shoe['agence'])
        sizes = await module.craw(shoe['detail_url'])
        shoe['size'] = sizes
    f.close()
    return

asyncio.get_event_loop().run_until_complete(start())