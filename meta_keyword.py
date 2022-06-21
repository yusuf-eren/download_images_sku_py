import pandas as pd
import numpy as np
import os
import re

df2 = pd.read_excel('TestReal.xlsx')
#print(df2.head())

#excell dosyamızın meta_keywords kısmında
#boşluklar yerine alt tire vardı
#bunları boşlukla replace ediyoruz
#siteye yüklerken sorun çıkmaması için
m_keywords = df2['meta_keywords(en-gb)']

for i in range(0, len(m_keywords)):
    m_keywords[i] = m_keywords[i].replace("_"," ", 50)

m_keywords.to_excel('meta_keyword.xlsx')