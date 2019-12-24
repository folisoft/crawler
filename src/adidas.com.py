import asyncio
import json
from pyppeteer import launch

_adidas_url = 'https://www.adidas.com/us/ultraboost-19-shoes/G27511.html'
_adidas_product_class = '.square-list ul li button'
_adidas_dropdown_class = 'gl-custom-dropdown__select'

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()

    # set timeout vi mang yeu
    await page.goto(_adidas_url, {'timeout': 80000, 'waitUntil': 'domcontentloaded'})
    if await page.J('.gl-modal__main-content'):
        await page.click('div > div > a')
    await page.click('.gl-custom-dropdown__select')

    product_sizes = await page.querySelectorAll(_adidas_product_class)
    f = open("output-adidas.com.json", "w")
    f.write("[")
    for size in product_sizes:
        itemSize = await page.evaluate('(element) => element.title', size)
        data = {}
        data['size'] = itemSize
        data['quantity'] = 3
        jsonData = json.dumps(data)
        f.writelines(jsonData + ', ')
    f.write("]")
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
