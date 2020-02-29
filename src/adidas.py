import asyncio
import json
from pyppeteer import launch

# _adidas_url = 'https://www.adidas.com/us/ultraboost-19-shoes/G27511.html'
_adidas_gender_class = '.gl-custom-dropdown__options span'
_adidas_sizes_class = '.square-list ul li'
async def craw(_adidas_url):
    browser = await launch({'headless': True})
    page = await browser.newPage()
    await page.setViewport({'width': 1600, 'height': 1300})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_adidas_url, {'timeout': 0})

    data_crawler = {}
    final_sizes = []

    # GENDER
    breadcrumb_query = "Array.from(document.querySelectorAll('"+_adidas_gender_class+"')).map(item => item.textContent);"
    breadcrumbs = await page.evaluate(breadcrumb_query, force_expr=True)
    gender = breadcrumbs[0]
    data_crawler['Gender'] = 'Men' if 'Men' in gender else 'Women'

    # SIZES
    query = "Array.from(document.querySelectorAll('"+_adidas_sizes_class+"')).map(item => item.title);"
    product_sizes = await page.evaluate(query, force_expr=True)
    for item in product_sizes:
        dataItem = {}
        dataItem['size'] = item
        dataItem['quantity'] = 3
        final_sizes.append(dataItem)
    data_crawler["sizes"] = final_sizes

    # WRITE TO FILE
    f = open("output-adidas.com.json", "w")
    f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()
    return data_crawler["sizes"]

# asyncio.get_event_loop().run_until_complete(main())
