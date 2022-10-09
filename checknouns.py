from konlpy.tag import Okt
from collections import Counter
import pandas as pd

f=open('btcdbd_nlp\\bitcoingallery_csv\\202209.csv','r',encoding='utf-8')
title=f.read()

okt = Okt()

noun=okt.nouns(title)
count = Counter(noun)

noun_list = count.most_common(300)
for v in noun_list:
    print(v)