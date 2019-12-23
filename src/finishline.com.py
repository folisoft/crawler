import asyncio
import json
from pyppeteer import launch

_finishline_url = 'https://www.finishline.com/store/product/womens-adidas-nmd-r1-casual-shoes/prod3030000?styleId=FW5278&colorId=001'
_finishline_product_class = '#productSizes .block-grid--sizes div button'

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()

    await page.goto(_finishline_url, { 'timeout': 80000, 'waitUntil': 'domcontentloaded' }) #set timeout vi mang yeu

    product_sizes = await page.querySelectorAll(_finishline_product_class)
    f = open("output-finishline.com.json", "w")
    f.write("[")
    for size in product_sizes:
        itemSize = await page.evaluate('(element) => element.dataset.size', size)
        sizeClass =(str)( await page.evaluate('(element) => element.className', size))
        data = {}
        if sizeClass.find('disabled') < 0 :
            data['size'] = itemSize
            data['quantity'] = 3
            jsonData = json.dumps(data)
            f.writelines(jsonData + ', ')
        else :
            data['size'] = itemSize
            data['quantity'] = 0
            jsonData = json.dumps(data)
            f.writelines(jsonData + ', ')

    f.write("]")
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())