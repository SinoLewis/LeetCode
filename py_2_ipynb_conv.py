import asyncio
import os
from os import listdir
from os.path import isfile, join

mypath = "<Your Python files directory to be converted>"

async def converter(file):
    # pip install p2j
    os.system(f"p2j {mypath}/{file}")

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    asyncio.run(converter(file))
