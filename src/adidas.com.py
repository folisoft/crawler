import asyncio
import json
from pyppeteer import launch

_adidas_url = 'https://www.adidas.com/us/ultraboost-19-shoes/G27511.html'
_adidas_gender_class = '.gl-custom-dropdown__options span'
_adidas_sizes_class = '.square-list ul li'
async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': 1600, 'height': 1300})
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36")
    await page.goto(_adidas_url, {'timeout': 0})

    default_men_sizes = ["4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10",
                         "10.5", "11", "11.5", "12", "12.5", "13", "13.5", "14", "14.5", "15", "16", "17", "18", "19"]
    default_women_sizes = ["5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5",
                           "10", "10.5", "11", "11.5", "12", "12.5", "13", "13.5", "14", "14.5", "15", "15.5"]

    data_crawler = {}
    sizes = []
    final_sizes = []

    breadcrumb_query = "Array.from(document.querySelectorAll('"+_adidas_gender_class+"')).map(item => item.textContent);"
    breadcrumbs = await page.evaluate(breadcrumb_query, force_expr=True)
    gender = breadcrumbs[0]

    query = "Array.from(document.querySelectorAll('"+_adidas_sizes_class+"')).map(item => item.title);"
    product_sizes = await page.evaluate(query, force_expr=True)

    if('Men' in gender ):
        sizes = default_men_sizes
    else:
        sizes = default_women_sizes

    data_crawler['Gender'] = 'Men' if 'Men' in gender else 'Women' 

    f = open("output-adidas.com.json", "w")

    for df_size in sizes:
        dataItem = {}
        dataItem['size'] = df_size
        index = product_sizes.count(df_size)
        if(index > 0):
            dataItem['quantity'] = 3
        else:
            dataItem['quantity'] = 0
        final_sizes.append(dataItem)

    data_crawler["sizes"] = final_sizes
    f.write(json.dumps(data_crawler))
    f.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
