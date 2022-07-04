#!/usr/bin/env python3

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)

