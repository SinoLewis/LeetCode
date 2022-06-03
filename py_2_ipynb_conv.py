import asyncio
# import subprocess
import os
from os import listdir
from os.path import isfile, join
from pprint import pprint

mypath = "<Your Python files directory to be converted>"

async def converter(file):
    # pip install p2j
    os.system(f"p2j {mypath}/{file}")
    # subprocess.run("/home/eren/.local/bin/p2j", f"{mypath}/{file}")

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    asyncio.run(converter(file))
