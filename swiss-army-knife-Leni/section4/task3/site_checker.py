#!/usr/bin/env python3

import requests

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://this-site-does-not-exist-12345.com"
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"{url} --> SITE UP (Status: {response.status_code})")
        else:
            print(f"{url} --> SITE DOWN (Status: {response.status_code})")

    except requests.RequestException:
        print(f"{url} --> SITE DOWN (Connection Failed)")
