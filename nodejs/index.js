const fs = require('fs');
const puppeteer = require('puppeteer');
const axios = require('axios');

(async () => {
    var browser = await puppeteer.launch({ 'headless': true });
    var page = await browser.newPage();
    await page.setViewport({ 'width': 1600, 'height': 1300 })
    await page.setUserAgent("Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/66.0.3359.181 Safari/537.36");
    // f = await fs.readFileSync('./input.json');
    // let products = JSON.parse(f);
    let get_products = await axios.get('http://oco.vn/api/export-url');
    let products = get_products.data;
    for (let index = 0; index < products.list.length; index++) {
        const item = products.list[index];
        let sizes = [];
        switch (item.agence) {
            case 'nike':
                sizes = await nike(item.detail_url, page);
                break;
            case 'adidas':
                sizes = await adidas(item.detail_url, page);
                break;
            case 'converse':
                sizes = await converse(item.detail_url, page);
                break;
            case 'finishline':
                sizes = await finishline(item.detail_url, page);
                break;
            case 'newbalance': //Need to update
                sizes = await newbalance(item.detail_url, page);
                break;
            default:
                break;
        }
        item['sizes'] = sizes;
    }
    // await fs.writeFileSync('./output.json', JSON.stringify(products)); //Test OUPUT FILE
    let response = await axios.post('http://oco.leo/api/update-quantity', JSON.stringify(products))
    console.log(response);
    await browser.close();
})();

async function nike(_nike_url, page) {
    _nike_gender_class = 'h2[data-test="product-sub-title"]'
    _nike_sizes_class = '#buyTools fieldset div > div > input'

    await page.goto(_nike_url, { 'timeout': 0 })

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
    for (let index = 0; index < cookies.length; index++) {
        const cooky = cookies[index];
        if (cooky.value == 'VN')
            await page.deleteCookie(delcooky)
    }
    await page.setCookie(cooky)
    await page.cookies('.nike.com')
    await page.reload({ 'waitUntil': ["networkidle0", "domcontentloaded"] })

    let data_crawler = {}
    let final_sizes = []

    // GENDER
    let gender_query = "Array.from(document.querySelectorAll('" + _nike_gender_class + "')).map(item => item.textContent);"
    let genders = await page.evaluate(gender_query, force_expr = true)

    data_crawler['Gender'] = genders[0] == 'Men' ? 'Men' : 'Women'

    // SIZES
    let query = "Array.from(document.querySelectorAll('" + _nike_sizes_class + "')).map(item => ({disabled: item.disabled, size: item.value.split(':')[1]}));"
    let product_sizes = await page.evaluate(query, force_expr = true);

    for (let index = 0; index < product_sizes.length; index++) {
        const item = product_sizes[index];
        let dataItem = {
            size: item.size,
            quantity: 3
        };
        if (item.disabled == true) dataItem.quantity = 0;
        final_sizes.push(dataItem);
    }
    data_crawler["sizes"] = final_sizes;

    return data_crawler["sizes"];

}

async function adidas(_adidas_url, page) {
    let _adidas_gender_class = '.gl-custom-dropdown__options span';
    let _adidas_sizes_class = '.square-list ul li';
    await page.goto(_adidas_url, { 'timeout': 0 })

    let data_crawler = {};
    let final_sizes = [];

    // GENDER
    let breadcrumb_query = "Array.from(document.querySelectorAll('" + _adidas_gender_class + "')).map(item => item.textContent);"
    let breadcrumbs = await page.evaluate(breadcrumb_query, force_expr = true);
    let gender = breadcrumbs[0];
    data_crawler['Gender'] = gender == 'Men' ? 'Men' : 'Women';

    // SIZES
    let query = "Array.from(document.querySelectorAll('" + _adidas_sizes_class + "')).map(item => item.title);"
    let product_sizes = await page.evaluate(query, force_expr = true);
    for (let index = 0; index < product_sizes.length; index++) {
        const item = product_sizes[index];
        let dataItem = {
            size: item,
            quantity: 3
        }
        final_sizes.push(dataItem)
    }
    data_crawler["sizes"] = final_sizes

    return data_crawler["sizes"]
}

async function converse(_converse_url, page) {
    let _converse_products_class = '#variationDropdown-size option';
    await page.goto(_converse_url, { 'timeout': 0 });

    let data_crawler = {};
    let final_sizes = [];
    let gender = "";

    let query = "Array.from(document.querySelectorAll('" + _converse_products_class + "')).map(item => item.textContent.trim());";
    let product_sizes_raw = await page.evaluate(query, force_expr = true);
    let product_sizes = [];
    for (let index = 0; index < product_sizes_raw.length; index++) {
        const value = product_sizes_raw[index];
        product_sizes.push(value)
    }

    let exist_men = product_sizes[1] == 'Men';
    let exist_women = product_sizes[1] == 'Women';

    // GENDER
    if (exist_men) gender = Men
    if (exist_women) gender = Women
    data_crawler["Gender"] = gender

    // SIZES
    for (let index = 0; index < product_sizes.length; index++) {
        const size = product_sizes[index];
        if (size == 'Men' || size == 'Women') {
            let size_number = size.split(' ');
            let dataItem = {
                size: size_number[1],
                quantity: 3
            };
            final_sizes.push(dataItem);
        }
    }
    data_crawler["sizes"] = final_sizes;

    return data_crawler['sizes'];
}

async function finishline(_finishline_url, page) {
    await page.goto(_finishline_url, { 'timeout': 0 });

    let data_crawler = {};
    let sizes = [];

    // GENDER
    let breadcrumb_query = "Array.from(document.querySelectorAll('" + _breadcrumbs_class + "')).map(item => item.textContent);";
    let breadcrumbs = await page.evaluate(breadcrumb_query, force_expr = true);
    let gender_object = breadcrumbs[1];
    data_crawler["gender"] = gender_object.strip();

    // SIZES
    let sizes_query = "Array.from(document.querySelectorAll('" + _finishline_product_class + "')).map(item => ({className: item.className, size: item.dataset.size}));";
    let product_sizes_raw = await page.evaluate(sizes_query, force_expr = true);
    let product_sizes = [];
    product_sizes = product_sizes_raw;
    for (let index = 0; index < product_sizes.length; index++) {
        const itemSize = product_sizes[index];
        let data = {
            size: itemSize.size,
            quantity: 3
        }
        if (itemSize['className'] == 'disabled') data['quantity'] = 0;
        sizes.push(data);
    }
    data_crawler["sizes"] = sizes;

    return data_crawler["sizes"];
}

async function newbalance(_detail_url, page) {
    // await page.goto(_detail_url, {'timeout': 0 })

    // let data_crawler = {};
    // let sizes = [];

    // // size listing
    // let document_query = "Array.from(document.querySelectorAll('.variant-select.size li')).map(x=> x.dataset.value );";
    // let sizes = await page.evaluate(document_query, force_expr=true);
    // let document_query = "Array.from(document.querySelectorAll('.variant-select.size li.unavailable')).map(x=> x.dataset.value );";
    // let unavailables = await page.evaluate(document_query, force_expr=true);

    // // check size available
    // for (let index = 0; index < sizes.length; index++) {
    //     const size = sizes[index];
    //     size_item = pydash.clone_deep(_size_item)

    //     size_item["size"] = size
    //     if size in unavailables:
    //         size_item['quantity'] = 3
    //     else:
    //         size_item['quantity'] = 0

    //     _output["sizes"].append(size_item)
    // }
    // for size in sizes:
    //     size_item = pydash.clone_deep(_size_item)

    //     size_item["size"] = size
    //     if size in unavailables:
    //         size_item['quantity'] = 3
    //     else:
    //         size_item['quantity'] = 0

    //     _output["sizes"].append(size_item)

    // return _output["sizes"]
    return [];
}