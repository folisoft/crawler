import asyncio
import json

_converse_products_class = '#variationDropdown-size option'

async def craw(_converse_url, page):
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

    return data_crawler['sizes']