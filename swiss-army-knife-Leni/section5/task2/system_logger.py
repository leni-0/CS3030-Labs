#!/usr/bin/env python3

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Script started")
logging.warning("Low disk space")
logging.error("Database connection failed")

print("Messages have been written to app.log")
