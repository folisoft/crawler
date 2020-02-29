---
page_type: sample
description: "This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask sample for Azure App Service (Linux)

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux.

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

ps -fA | grep python

#   Debug
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=application.py
flask run

FLASK_APP=application.py FLASK_ENV=development flask run
$ FLASK_APP=main.py FLASK_ENV=development flask run --port 8080

1.  triggers
2.  job stores
3.  executors
4.  schedulers

 signal only works in main thread

 pip3 install virtualenv
 pip3 install -r requirements.txt

https://github.com/viniciuschiele

https://www.programcreek.com/python/example/103359/apscheduler.schedulers.blocking.BlockingScheduler

# Environment tips
    pip3 install -r requirements.txt

    On new MAC, I have the problem when I running the python 3. It can't download package yuppeeter.
    And I solved by research and run the command in below:
    pip install -U "urllib3<1.25"


