import asyncio
from pyppeteer import launch

#   Crawler
    # We crawl the product by url https://www.nike.com/w?q=AT6174-005
    # And check the product on the url http://oco.vn/san-pham?q=AT6174-005

    # This is the list of SKU for testing:
    # 13	AT6174-005	NIKE AIR MAX 270 REACT	Women	4,449,000	Stocking	
    # 14	AT6174-100	NIKE AIR MAX 270 REACT	Women	4,199,000	Stocking	
    # 15	AT6174-102	NIKE AIR MAX 270 REACT	Women	4,199,000	Stocking	
    # 16	AT6174-700	NIKE AIR MAX 270 REACT	Women	4,199,000	Stocking

_nike_url = 'https://www.nike.com/w?q=AT6174-005'
_nike_product_class = '.product-card__body'
_nike_product_price = '.original-price'


async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()

    await page.goto(_nike_url)
    
    # document.querySelectorAll('.product-card__body')[0]
    product_el = await page.querySelector(_nike_product_class)
    await page.click(_nike_product_class)

    # document.querySelectorAll('.original-price')[0].innerText
    product_el_price = await page.querySelector(_nike_product_price)
    product_price = await page.evaluate('(element) => element.textContent', product_el_price)
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())