import asyncio
import json
from pyppeteer import launch

_adidas_url = 'https://www.adidas.com/us/ultraboost-19-shoes/G27511.html'
_adidas_product_class = '.gl-custom-dropdown--no-max-height > select > option'
_adidas_button_class = '.gl-custom-dropdown--no-max-height > button'

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()

    # set timeout vi mang yeu
    await page.goto(_adidas_url, {'timeout': 80000, 'waitUntil': 'load'})

    # if await page.J('#modal-root .gl-modal'):
    #     await page.click('button')

    # product_sizes = await page.querySelectorAll('.gl-custom-dropdown--no-max-height select option')
    await page.waitForSelector('.square-list ul li', {'timeout': 300000})
    product_sizes = await page.querySelectorAll('.square-list ul li')
    f = open("output-adidas.com.json", "w")
    # f.write("[")
    # for size in product_sizes:
    #     itemSize = await page.evaluate('(element) => element.title', size)
    #     data = {}
    #     data['size'] = itemSize
    #     data['quantity'] = 3
    #     jsonData = json.dumps(data)
    #     f.writelines(jsonData + ', ')
    # f.write("]")
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
