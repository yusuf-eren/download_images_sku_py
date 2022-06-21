import pandas as pd
import numpy as np
import os
import re

df5 = pd.read_excel('sku_seo.xlsx')

dir = df5['sku']
try:
    for i in range(0, len(dir)):
        dir[i] = ('catalog/urunler/all_rugs_bulk/' + dir[i] + '.jpg')
except:
    pass
dir.to_excel('image_dir.xlsx')