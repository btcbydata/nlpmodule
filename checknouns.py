from konlpy.tag import Okt
from collections import Counter
import pandas as pd

f=open('빗갤원본\\202101.csv','r',encoding='utf-8')
title=f.read()

okt = Okt()

noun=okt.nouns(title)
count = Counter(noun)

noun_list = count.most_common(300)



for v in noun_list:
    print(v)