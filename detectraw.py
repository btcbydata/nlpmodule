import pandas as pd

data = pd.read_csv("btcbd_nlp\\bitcoingallery_csv\\202001.csv")

data = data.drop(['date'],axis=1)
df = data[data['title'].str.contains('비트')]
df.to_csv("bit.csv", encoding='utf-8-sig')


"""

word match
BITCOIN = "비트" FLOW = "플로우" NEM = "넴" TOPSHOT = "탑샷" CARDANO = "카르" ANKER = "앵커" ARGO = "아르고" METAL = "메탈" EDchain = "에드" ORBS = "오브스" CSPR = "캐스퍼" MARO = "마로" LUNA = "루나" PUNDIX = "펀디" MVL = "엠블" ENJIN = "엔진" MBL = "무비" PXL = "픽셀" MANA = "마나" TRON = "트론" HBAR = "헤데" CHR = "크로미아"

"""
