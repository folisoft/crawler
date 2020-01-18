#   Crawler
    # We crawl the product by url https://www.nike.com/w?q=AT6174-005
    # And check the product on the url http://oco.vn/san-pham?q=AT6174-005

    # This is the list of SKU for testing:
    # 13	AT6174-005	NIKE AIR MAX 270 REACT	Women	4,449,000	Stocking	
    # 14	AT6174-100	NIKE AIR MAX 270 REACT	Women	4,199,000	Stocking	
    # 15	AT6174-102	NIKE AIR MAX 270 REACT	Women	4,199,000	Stocking	
    # 16	AT6174-700	NIKE AIR MAX 270 REACT	Women	4,199,000	Stocking

import asyncio
import json
from pyppeteer import launch
import pydash
import json

_output = {
    "name": "Women's adidas NMD R1 Casual Shoes",
    "gender": "Women",
    "sizes": []
}

_size_item = {
    "size": "5.5",
    "quantity": 0
}

_page_name = 'nike.com'
_detail_url = 'https://www.nike.com/t/air-max-270-react-womens-shoe-6KXPPH/AT6174-200'

async def main():
    # pyppeteer
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_detail_url, {'timeout': 0 })

    # product name
    class_name = '#pdp_product_title'
    element = await page.querySelector(class_name)
    content = await page.evaluate('(element) => element.textContent', element)
    _output["name"] = content.strip()

    # gender
    class_name = '.headline-5.pb1-sm'
    element = await page.querySelector(class_name)
    content = await page.evaluate('(element) => element.textContent', element)
    _output["gender"] = content.strip()

    # size listing
    class_name = '.css-1uentg input'
    await page.waitForSelector(".css-1uentg input", { "visible": True })
    document_query = "Array.from(document.querySelectorAll('.css-1uentg input')).map(x=> {return {quantity: (x.disabled ? 3 : 0), size: (x.value.split(':')[1])}});"
    sizes = await page.evaluate(document_query, force_expr=True)

    print(sizes)
    _output["sizes"] = sizes

    # file json
    f = open(_page_name+'.json', "w")
    f.write(json.dumps(_output))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
