import asyncio
import json
from pyppeteer import launch

_converse_url = 'https://www.converse.com/shop/p/chuck-taylor-all-star-unisex-lowtopshoe/M7652.html?cgid=mens-best-sellers&dwvar_M7652_color=optical%20white&dwvar_M7652_size=065&styleNo=M7652&pdp=true'
_converse_products_class = '#variationDropdown-size option'


async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': 1600, 'height': 1300})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_converse_url, {'timeout': 0})

    data_crawler = {}
    final_sizes = []
    gender = ""
    Men = "Men"
    Women = "Women"

    query = "Array.from(document.querySelectorAll('" + _converse_products_class + "')).map(item => item.textContent.trim());"
    product_sizes_raw = await page.evaluate(query, force_expr=True)
    product_sizes = []
    for value in product_sizes_raw:
        product_sizes.append(value)

    exist_men = True if Men in product_sizes[1] else False
    exist_women = True if Women in product_sizes[1] else False

    # GENDER
    if(exist_men):
        gender = Men
    if(exist_women):
        gender = Women
    data_crawler["Gender"] = gender

    # SIZES
    for size in product_sizes:
        if(Men in size or Women in size):
            dataItem = {}
            size_number = size.split(' ')
            dataItem['size'] = size_number[1]
            dataItem['quantity'] = 3
            final_sizes.append(dataItem)

    data_crawler["sizes"] = final_sizes

    # WRITE TO FILE
    f = open("output-converse.com.json", "w")
    f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
