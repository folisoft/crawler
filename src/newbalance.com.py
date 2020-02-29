import asyncio
import json
from pyppeteer import launch
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

_page_name = 'newbalance.com'
_detail_url = 'https://www.newbalance.com/pd/fresh-foam-roav-city-grit/MROAVV1-28556-M.html?dwvar_MROAVV1-28556-M_color=Natural%20Indigo_with_Light%20Slate#color=Stone%20Blue_with_Neo%20Crimson'


async def main():
    # pyppeteer
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_detail_url, {'timeout': 0 })
    # await page.goto(_detail_url, {'waitUntil': 'domcontentloaded' })
    

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
    
    # file json
    f = open(_page_name+'.json', "w")
    f.write(json.dumps(_output))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
