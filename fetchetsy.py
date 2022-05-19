import shutil
import requests
import os
import pandas as pd

# Getting Columns
df1 = pd.read_excel('etsy_sku_i.xlsx')
list_sku1 = list(df1['SKU'])
list_image1 = list(df1['IMAGE1'])

# We are going to fetch all links in list_image1
for i in list_image1:
    r = requests.get(i).content
    # Naming photos with their SKUs
    for x in range(0, len(list_sku1)):
        with open((str(list_sku1[x]) + ".jpg"),"wb+") as f:
            f.write(r)