#!/usr/bin/env python3

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

webhook_url = os.getenv("WEBHOOK_URL")

if not webhook_url:
    print("Error: WEBHOOK_URL not found in .env")
    exit(1)

message = {
    "content": "ALERT: System monitor detected an issue!"
}

try:
    response = requests.post(webhook_url, json=message, timeout=10)

    if response.status_code in (200, 204):
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.RequestException as e:
    print(f"Error sending notification: {e}")
