import pandas as pd
import numpy as np
import os
import re

df6 = pd.read_excel('TestReal.xlsx')
#print(df2.head())

m_title = df6['meta_title(en-gb)']

#title'ın sonuna | Siteadi.com ekliyoruz.
#bu sayede her ürünün title'ı tekrar yazmak
#zorunda kalmayacağız.
try:
    for i in range(0, len(m_title)):
        m_title[i] = m_title[i] + ' | Rugbuying.com'
except:
    pass
m_title.to_excel('meta_title.xlsx')