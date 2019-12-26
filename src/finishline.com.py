import asyncio
import json
from pyppeteer import launch

_finishline_url = 'https://www.finishline.com/store/product/womens-adidas-nmd-r1-casual-shoes/prod3030000?styleId=FW5278&colorId=001'

_finishline_product_class = '#productSizes .block-grid--sizes div button'
_breadcrumbs_class = '.breadcrumbs li a span'

_shoes_name_class = '#title'

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()

    await page.goto(_finishline_url, { 'timeout': 80000, 'waitUntil': 'domcontentloaded' }) #set timeout vi mang yeu

    data_crawler = {}
    sizes = []
    # NAME OF SHOES
    shoesnames = await page.querySelector(_shoes_name_class)
    shoesname = await page.evaluate('(element) => element.textContent', shoesnames)
    data_crawler["name"] = shoesname.strip()

    # GENDER
    breadcrumbs = await page.querySelectorAll(_breadcrumbs_class)
    gender_object = await page.evaluate('(element) => element.textContent', breadcrumbs[1])
    data_crawler["gender"] = gender_object.strip()

    f = open("output-finishline.com.json", "w")
    product_sizes = await page.querySelectorAll(_finishline_product_class)
    for size in product_sizes:
        itemSize = await page.evaluate('(element) => element.dataset.size', size)
        sizeClass =(str)( await page.evaluate('(element) => element.className', size))
        data = {}
        if sizeClass.find('disabled') < 0 :
            data['size'] = itemSize
            data['quantity'] = 3
        else :
            data['size'] = itemSize
            data['quantity'] = 0
        sizes.append(data)
    data_crawler["sizes"] = sizes
    f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())