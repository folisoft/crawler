import asyncio
import json
from pyppeteer import launch

_adidas_url = 'https://www.adidas.com/us/ultraboost-19-shoes/G27511.html'
_adidas_product_class = '.gl-custom-dropdown--no-max-height > select > option'
_adidas_button_class = '.gl-custom-dropdown--no-max-height > button'


async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_adidas_url, {'timeout': 0})

    data_crawler = {}
    sizes = []

    # product_sizes = await page.querySelectorAll('.gl-custom-dropdown--no-max-height select option')


    # await page.waitForSelector('.square-list ul li', {'timeout': 0})
    # product_sizes = await page.querySelectorAll('.square-list ul li')
    query = "Array.from(document.querySelectorAll('.square-list ul li')).map(item => item.title);"
    product_sizes = await page.evaluate(query, force_expr=True)

    f = open("output-adidas.com.json", "w")
    # for size in product_sizes:
    #     itemSize = await page.evaluate('(element) => element.title', size)
    #     dataItem = {}
    #     dataItem['size'] = itemSize
    #     dataItem['quantity'] = 3
    #     sizes.append(dataItem)
    # data_crawler["sizes"] = sizes
    # f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
