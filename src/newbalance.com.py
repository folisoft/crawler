import asyncio
import json
import pydash
import json

_output = {
    "name": "Women's adidas NMD R1 Casual Shoes",
    "gender": "Women",
    "sizes": [{
        "size": "5.5",
        "quantity": 0
    }]
}

_size_item = {
    "size": "5.5",
    "quantity": 0
}

async def craw(_detail_url, page):
    await page.goto(_detail_url, {'timeout': 0 })

    # product name
    class_name = '.product-name'
    element = await page.querySelector(class_name)
    content = await page.evaluate('(element) => element.textContent', element)
    _output["name"] = content.strip()

    # gender
    class_name = '.gender-type'
    element = await page.querySelector(class_name)
    content = await page.evaluate('(element) => element.textContent', element)
    _output["gender"] = content.strip()

    # size listing
    class_name = '.variant-select.size li'
    document_query = "Array.from(document.querySelectorAll('.variant-select.size li')).map(x=> x.dataset.value );"
    sizes = await page.evaluate(document_query, force_expr=True)
    document_query = "Array.from(document.querySelectorAll('.variant-select.size li.unavailable')).map(x=> x.dataset.value );"
    unavailables = await page.evaluate(document_query, force_expr=True)

    # check size available
    for size in sizes:
        size_item = pydash.clone_deep(_size_item)

        size_item["size"] = size
        if size in unavailables:
            size_item['quantity'] = 3
        else:
            size_item['quantity'] = 0

        _output["sizes"].append(size_item)

    return _output["sizes"]