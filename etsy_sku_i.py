import pandas as pd
import numpy as np
import os
import re

df9 = pd.read_excel('etsy_sku_i.xlsx')

dir = df9['SKU']
try:
    for i in range(0, len(dir)):
        dir[i] = ('catalog/urunler/all_rugs_bulk/' + str(dir[i]) + '.jpg')
except:
    pass
dir.to_excel('SKU_FINAL.xlsx')