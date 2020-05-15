#!/usr/bin/env python3

from json import dumps
import os, sys, requests

if 'GOOGLE_CHAT_WEBHOOK' not in os.environ:
    print("no google chat webhook found")
    sys.exit(0)

url = os.environ['GOOGLE_CHAT_WEBHOOK']
bot_message = {
    'text' : "smartd warning: {}\n  device: {} ({})".format(os.environ['SMARTD_MESSAGE'],os.environ['SMARTD_DEVICEINFO'],os.environ['SMARTD_DEVICE'])
    }

headers = {'Content-Type': 'application/json; charset=UTF-8'}

response = requests.post(url, data=dumps(bot_message), headers=headers)

if response.status_code != 200:
    print(response.status_code,response.content)
