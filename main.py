#!/bin/python3

import requests
from PIL import Image
from io import BytesIO
import re

with open("./input.txt") as file:
    lines = file.readlines()
    for line in lines:
        url = line.strip()
        
        m = re.search("(kulturne-objekty|cultural-objects)/([a-z0-9\-]+)\??", url)
        if m == None:
            print("URL neobsahuje ID.")
            continue

        uid = m.group(2)
        x = requests.get("https://wcm.slovakiana.sk/culturalobject/"+uid, verify=False)
        id = x.json()['digitalObjects'][0]['id']
        y = requests.get("https://wcm.slovakiana.sk/digitalobject/"+id, verify=False)
        for c in y.json()['content'][0]['images']:
            for q in range(15):
                if c['fileId'] == 'CAIR_FILE_'+str(q):
                    r = requests.get(c['full']['fileUrl'], verify=False)
                    i = Image.open(BytesIO(r.content))
                    i.save(uid+"_"+str(q)+".jp2")