#!/usr/bin/env python3

import shutil
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")
backup_name = f"backup-{today}"
shutil.make_archive(backup_name, "zip", "/home/leni/CS3030/CS3030-Labs/swiss-army-knife-Leni/section1")
print(f"Created {backup_name}.zip")
