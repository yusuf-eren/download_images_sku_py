import shutil
import requests
import os
import pandas as pd

# Excell Dosyamızın Kolonlarını Alıyoruz
df1 = pd.read_excel('etsy_sku_i.xlsx')
list_sku1 = list(df1['SKU'])
list_image1 = list(df1['IMAGE1'])

# list_image1 içindeki ürünleri çekip isimlerini
# stok koduyla kaydediyoruz
for i in range(0,len(list_image1)):
    r = requests.get(list_image1[i]).content
    # Naming photos with their SKUs
    with open((str(list_sku1[i]) + ".jpg"),"wb+") as f:
        f.write(r)
        