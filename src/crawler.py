import asyncio
import json

async def start():
    f = open('./input.json')
    products = json.load(f)
    f.close()
    for shoe in products['list']:
        module = __import__(shoe['agence'])
        sizes = await module.craw(shoe['detail_url'])
        if sizes is not None :
            shoe['sizes'] = sizes
    fileOutput = open('./output.json','w')
    fileOutput.write(json.dumps(products))
    fileOutput.close()
    return

asyncio.get_event_loop().run_until_complete(start())