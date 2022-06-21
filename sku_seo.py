import pandas as pd
import numpy as np
import os
import re

df3 = pd.read_excel('TestReal.xlsx')

#ürünün seo linkini our-rugs- + stok kodu
#şeklinde kaydediyoruz
sku = df3['sku']
try:
    for i in range(0, len(sku)):
        sku[i] = "our-rugs-" + str(sku[i])
except:
    pass
sku.to_excel('sku_seo.xlsx')