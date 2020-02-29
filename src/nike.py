import asyncio
import json
from pyppeteer import launch

# _nike_url = 'https://www.nike.com/t/air-max-270-react-womens-shoe-6KXPPH/AT6174-200'
_nike_gender_class = 'h2[data-test="product-sub-title"]'
_nike_sizes_class = '#buyTools fieldset div > div > input'


async def craw(_nike_url, page):
    await page.goto(_nike_url, {'timeout': 0})

    cooky = {
        'name': 'NIKE_COMMERCE_COUNTRY',
        'value': 'US',
        'domain': '.nike.com'
    }
    delcooky = {
        'name': 'NIKE_COMMERCE_COUNTRY',
        'value': 'VN',
        'domain': '.nike.com'
    }
    cookies = await page.cookies('https://www.nike.com')
    for item in cookies:
        if item['value'] == 'VN':
            await page.deleteCookie(delcooky)
            await page.setCookie(cooky)
            await page.cookies('.nike.com')
            await page.reload({'waitUntil': ["networkidle0", "domcontentloaded"]})

    data_crawler = {}
    final_sizes = []

    # GENDER
    gender_query = "Array.from(document.querySelectorAll('"+ _nike_gender_class+"')).map(item => item.textContent);"
    genders = await page.evaluate(gender_query, force_expr=True)

    data_crawler['Gender'] = 'Men' if 'Men' in genders[0] else 'Women'

    # SIZES
    query = "Array.from(document.querySelectorAll('"+_nike_sizes_class +"')).map(item => ({disabled: item.disabled, size: item.value.split(':')[1]}));"
    product_sizes = await page.evaluate(query, force_expr=True)
    for item in product_sizes:
        dataItem = {}
        dataItem['size'] = item['size']
        dataItem['quantity'] = 3
        if item['disabled'] == True:
            dataItem['quantity'] = 0
        final_sizes.append(dataItem)
    data_crawler["sizes"] = final_sizes

    return data_crawler["sizes"]
