#!/usr/bin/env python3

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

secret_key = os.getenv("SUPER_SECRET_KEY")

if secret_key:
    masked_key = "*" * (len(secret_key) - 3) + secret_key[-3:]
    print(f"Accessing system with key: {masked_key}")
else:
    print("Error: SUPER_SECRET_KEY not found.")
