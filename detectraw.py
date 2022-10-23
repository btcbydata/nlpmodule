import pandas as pd
import os

filename = "202209"
## files = os.listdir('btcbd_nlp\\bitcoingallery_csv')
data = pd.read_csv("btcbd_nlp\\bitcoingallery_csv\\"+filename+".csv")


data = data.drop(['date'],axis=1)
df = data[data['title'].str.contains(' 비트|플로우|넴|이더|이클|플로우|넴|탑샷|카르|앵커|아르고|메탈|에드|오브스|캐스퍼|마로|루나|펀디|엠블|엔진|무비|픽셀| 마나|트론|헤데|크로미아|방카|보바|이더|테더|리플|도지|솔라나|체인링크|트론|아발|유니|이클|위믹스|팬케이크|빗골| 라코|이오스|비캐|빗캐|스텔라|슨트|카이버|스텔라|클레|크레딧|헤데라')]
df.to_csv(filename+"_result.csv", encoding='utf-8-sig')

print(filename + " completed")


"""

word match
BITCOIN = "비트" FLOW = "플로우" NEM = "넴" TOPSHOT = "탑샷" CARDANO = "카르" ANKER = "앵커" ARGO = "아르고" METAL = "메탈" EDchain = "에드" ORBS = "오브스" CSPR = "캐스퍼" MARO = "마로" LUNA = "루나" PUNDIX = "펀디" MVL = "엠블" ENJIN = "엔진" MBL = "무비" PXL = "픽셀" MANA = "마나" TRON = "트론" HBAR = "헤데" CHR = "크로미아" BANCA = "방카" BOBA = "보바" ETHERIUM = "이더" TETHER = "테더" XRP = "리플" DOGECOIN = "도지" SOLANA = "솔라나" CHAINLINK = "체인링크" TRON = "트론" AVALANCHE = "아발" UNISWAP = "유니" ETHERIUM CLASSIC = "이클" WEMIX = "위믹스" PANCAKESWAP = "팬케이크" BITCOIN GOLD = "빗골" LITECOIN = "라코" (*보/라코/인, 솔/라코/인 등과 겹침) -> 공백 EOS = "이오스" BITCOIN CASH = "비캐,빗캐" STELLAR = "스텔라" SNT = "슨트" KAIBER = "카이버" STELLAR LUMEN = "스텔라" KLATON = "클레" CREDIT = "크레딧" HEDERA = "헤데라"

"""
