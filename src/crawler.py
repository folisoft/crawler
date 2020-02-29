import asyncio
import json
from pyppeteer import launch
import requests

async def getInput():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.status_code)
    print(response.json())

async def start():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': 1600, 'height': 1300})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    f = open('./input.json')
    products = json.load(f)
    f.close()
    for shoe in products['list']:
        module = __import__(shoe['agence'])
        print(shoe['detail_url'])
        sizes = await module.craw(shoe['detail_url'], page)
        if sizes is not None :
            shoe['sizes'] = sizes
    fileOutput = open('./output.json','w')
    fileOutput.write(json.dumps(products))
    fileOutput.close()
    await browser.close()
    return

asyncio.get_event_loop().run_until_complete(start())