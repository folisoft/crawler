import asyncio
import json

_adidas_gender_class = '.gl-custom-dropdown__options span'
_adidas_sizes_class = '.square-list ul li'

async def craw(_adidas_url, page):
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

    return data_crawler["sizes"]