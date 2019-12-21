# webcrawlers-nodejs-python-nodejs-RESTful-API
The Node js web crawler uses puppeteer and loads data to a sqlite3 database. 
The python version uses requests_html and HTML, AsyncHTMLSession.
Restful Apis with Nodejs, Express, Ejs, sqlite3 Database queries,  D3 graphs and canvas javascript to create 
dynamic websites

# https://github.com/bebooth2/webcrawlers-nodejs-python-nodejs-RESTful-API

# Author Briann Booth <Data Science>
Masters in Applied Mathematics and Computer Science. Undergrad minor in Physics. Interest in finance, passed the SOA's P and Fm exams
https://github.com/bebooth2

#   Environment on my PC 
    python --version && node --version && npm --version && pip3 --version
    
    Information on my MAC:
    -   Python 2.7.16
    -   v13.1.0
    -   6.13.1
    -   pip 19.0.3 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

    -   SQLite3
    https://www.sqlite.org/download.html (*)
    https://www.quackit.com/sqlite/tutorial/sqlite_installation.cfm
    https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite (*)
    https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv (*)

#   RestfullApi
    0.  cd nodejs && ncu && ncu -u && nodemon start
    1.  Install latest nodejs https://nodejs.org/en/
    3.  npm i -g express-generator nodemon npm-check-updates
    4.  express --view=ejs mywebsite && cd mywebsite && npm i && nodemon start

    REF: https://medium.com/@bhanushali.mahesh3/creating-a-simple-website-with-node-js-express-and-ejs-view-engine-856382a4578f

#   NodeJS (Ctr + C => break cli)
    0.  Up to date for all the dependencies packages:
        "dependencies": {
            "cookie-parser": "~1.4.4",
            "debug": "~2.6.9",
            "ejs": "~2.6.1",
            "express": "~4.16.1",
            "http-errors": "~1.6.3",
            "morgan": "~1.9.1",
            "sqlite3": "^4.1.1"
        }
    1.  cd nodejs && ncu && ncu -u && nodemon start

#   python (Ctr + D => break cli)
    0.  cd python && pip run
    1.  pip3 install requests-html
    2.  pip3 install pysqlite3

    REF: 
    https://www.w3schools.com/python/python_reference.asp
    https://www.w3schools.com/xml/xpath_intro.asp

#   GraphQL

    
    filter=attributeIds(16633190-45e5-4830-a068-232ac7aea82c,193af413-39b0-4d7e-ae34-558821381d3f)&anchor=24&count=24&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647
    filter=attributeIds(16633190-45e5-4830-a068-232ac7aea82c,193af413-39b0-4d7e-ae34-558821381d3f)&anchor=48&count=24&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647