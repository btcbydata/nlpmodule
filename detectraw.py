import pandas as pd

id = []
document = []
label = []
filename='testdata'

data=pd.read_csv("btcdbd_nlp\\bitcoingallery_csv\\202001.csv")

data.query('title.str.contains("비트")')

data