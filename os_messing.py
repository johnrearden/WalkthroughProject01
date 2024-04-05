import os
import json
from pathlib import Path

from datetime import datetime

basepath = Path('')

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y, %H:%M:%S')
    return formatted_date

with os.scandir() as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(f'{entry.name}, last modified on {convert_date(info.st_mtime)}')

