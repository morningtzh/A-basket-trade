
# In[]
import jqdatasdk
import pandas as pd
import os

from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

# ID是申请时所填写的手机号；Password为聚宽官网登录密码，新申请用户默认为手机号后6位
jqdatasdk.auth('18605712083', 'sbbuzhidaomima')


# # In[]

# all_securities = jqdatasdk.get_all_securities(['stock', 'fund', 'index', 'futures', 'options', 'etf', 'lof',
#                                                'fja', 'fjb', 'open_fund', 'bond_fund', 'stock_fund', 'QDII_fund', 'money_market_fund', 'mixture_fund'])

# In[]

a = pd.read_csv("./data/csv/all_securities.csv")
jqdatasdk.get_query_count()
# In[]

all_index = a[a["type"] == "index"]

for security in all_index.iloc[:, 0]:

    if os.path.exists("./data/csv/daily/{security}.csv".format(security=security)):
        continue
    
    security_bar = jqdatasdk.get_bars("000016.XSHG", 3650, unit='1d',
                        fields=['date', 'open', 'close', 'high', 'low', 'volume', 'money'],
                        include_now=False, end_dt=None, fq_ref_date=None)

    security_bar.to_csv("./data/csv/daily/{security}.csv".format(security=security),index=False)


#In[]

# {
#     "code": 0, 
#     "msg": null, 
#     "data": {
#         "fields": ["ts_code", "trade_date", "pre_close", "open", "high", "low", "close", "change", "pct_chg", "vol", "amount"], 
#         "items": [
#             ["500029.SH", "20050105", 0.8670, 0.8660, 0.8740, 0.8640, 0.8700, 0.0030, 0.3460, 26342.1600, 2285.0670], 
#             ["184700.SZ", "20050105", 0.7270, 0.7290, 0.7310, 0.7200, 0.7250, -0.0020, -0.2751, 18001.4400, 1303.6421], 
#             ["184706.SZ", "20050105", 0.5350, 0.5350, 0.5390, 0.5340, 0.5360, 0.0010, 0.1869, 42184.5200, 2259.8744], 
#             ["500008.SH", "20050105", 0.8850, 0.8850, 0.8890, 0.8810, 0.8870, 0.0020, 0.2260, 13427.7000, 1186.3540], 
#             ["160813.SZ", "20050105", 0.5520, 0.5510, 0.5550, 0.5500, 0.5520, 0.0000, 0.0000, 29766.0000, 1644.3028], 
#             ["160919.SZ", "20050105", 0.5700, 0.5720, 0.5730, 0.5690, 0.5700, 0.0000, 0.0000, 17263.6400, 984.2873]
#             ]
#             }
# }

import json
import datetime
import os

security_bars = {}

daily_file_list = os.listdir("./data/roowe/ts/fund/fund_daily/")

print("start at ", datetime.datetime.now())

for file_name in daily_file_list:
    with open("./data/roowe/ts/fund/fund_daily/" + file_name) as data:
        json_date = json.loads(data.read())["data"]
        for daily_json in json_date["items"]:
            if daily_json[0] not in security_bars:
                security_bars[daily_json[0]] = []

            security_bars[daily_json[0]].append(daily_json)
    print(file_name, "read end at ", datetime.datetime.now())

print("read end at ", datetime.datetime.now())

#In[]
import pandas as pd
import numpy as np

for index, data in security_bars.items():
    security_df = pd.DataFrame(
        np.array(data), 
        columns=[
            "ts_code", 
            "trade_date", 
            "pre_close", 
            "open", 
            "high", 
            "low", 
            "close", 
            "change", 
            "pct_chg", 
            "vol", 
            "amount"]
            )
    print(index, "security_df end at ", datetime.datetime.now())

    security_df.to_csv("./data/csv/daily2/{security}.csv".format(security=index),index=False)

# %%
for index, data in security_bars.items():
    print(data)
    break

#%%
