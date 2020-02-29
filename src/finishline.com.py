import asyncio
import json

_finishline_product_class = '#productSizes .block-grid--sizes div button'
_breadcrumbs_class = '.breadcrumbs li a span'

_shoes_name_class = '#title'

async def craw(_finishline_url, page):
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

    return data_crawler["sizes"]
