import os
import json

entries = os.scandir()
for entry in entries:
    print(entry)


