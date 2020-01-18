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
    await page.setViewport({'width': 1600, 'height': 1300})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_finishline_url, {'timeout': 0})

    data_crawler = {}
    sizes = []

    # GENDER
    breadcrumb_query = "Array.from(document.querySelectorAll('"+_breadcrumbs_class+"')).map(item => item.textContent);"
    breadcrumbs = await page.evaluate(breadcrumb_query, force_expr=True)
    gender_object = breadcrumbs[1]
    data_crawler["gender"] = gender_object.strip()

    # SIZES
    sizes_query = "Array.from(document.querySelectorAll('"+_finishline_product_class+"')).map(item => ({className: item.className, size: item.dataset.size}));"
    product_sizes_raw = await page.evaluate(sizes_query, force_expr=True)
    product_sizes = []
    for item in product_sizes_raw:
        product_sizes.append(item)
    for itemSize in product_sizes:
        data = {}
        if 'disabled' in itemSize['className'] :
            data['size'] = itemSize['size']
            data['quantity'] = 0
        else:
            data['size'] = itemSize['size']
            data['quantity'] = 3
        sizes.append(data)
    data_crawler["sizes"] = sizes

    # WRITE TO FILE
    f = open("output-finishline.com.json", "w")
    f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
