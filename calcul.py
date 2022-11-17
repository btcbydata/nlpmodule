
import re

#filename=str(202210_1)

f=open('월별코인별데이터\\분석결과\\202208_1.txt',mode='r',encoding='utf-8')
lines = f.readlines()
cnt=0
negative=0
positive=0

for line in lines:
    templist=re.findall(r"[-+]?(?:\d*\.\d+|\d+)",line)
    if not templist:
        break #마지막 줄 처리
    cnt+=1
    negative+=float(templist[0])
    positive+=float(templist[1])

print("비트 : %f %f"%(negative/cnt,positive/cnt))
print("valid : ",cnt)

'''
import os
import pandas as pd

files = os.listdir("빗갤원본")
files


for i in files:
    data = pd.read_csv("빗갤원본\\"+i)
    print(i)
    print(len(data.index))

'''