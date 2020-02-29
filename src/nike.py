import asyncio
import json
from pyppeteer import launch

# _nike_url = 'https://www.nike.com/t/air-max-270-react-womens-shoe-6KXPPH/AT6174-200'
_nike_gender_class = 'h2[data-test="product-sub-title"]'
_nike_sizes_class = '#buyTools fieldset div > div > input'
async def craw(_nike_url):
    browser = await launch({'headless': True})
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.setViewport({'width': 1600, 'height': 1300})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_nike_url, {'timeout': 0})

    data_crawler = {}
    final_sizes = []

    # GENDER
    gender_query = "Array.from(document.querySelectorAll('"+_nike_gender_class+"')).map(item => item.textContent);"
    genders = await page.evaluate(gender_query, force_expr=True)

    data_crawler['Gender'] = 'Men' if 'Men' in genders[0] else 'Women'

    # SIZES
    query = "Array.from(document.querySelectorAll('"+_nike_sizes_class+"')).map(item => ({disabled: item.disabled, size: item.value.split(':')[1]}));"
    product_sizes = await page.evaluate(query, force_expr=True)
    for item in product_sizes:
        dataItem = {}
        dataItem['size'] = item['size']
        dataItem['quantity'] = 0 if item['disabled'] == 'true' else 3
        final_sizes.append(dataItem)
    data_crawler["sizes"] = final_sizes

    # WRITE TO FILE
    f = open("output-nike.com.json", "w")
    f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()
    return data_crawler["sizes"]