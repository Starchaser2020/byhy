import matplotlib.pyplot as plt
import requests, csv
from datetime import datetime
import pandas as pd
import numpy as np
import traceback


plt.rcParams['font.family'] = 'sans-serif'
# 设定字体为微软雅黑
plt.rcParams['font.sans-serif']=['Microsoft Yahei']

def stockinfo(code,startdate,enddate):
    payload = {'code': code, 'start': startdate, 'end': enddate}
    res = requests.get("http://q.stock.sohu.com/hisHq", params=payload)
    retObj = res.json()

    historyData = retObj[0]['hq']

    dateList = []
    closePriceList = []
    for dayInfo in historyData:
        # 获取收盘价
        dateList.append(dayInfo[0])
        closePriceList.append(float(dayInfo[2]))

    data = np.array([dateList,closePriceList]).T

    df = pd.DataFrame(data,columns=['日期','收盘价'])
    print(df.head())
    df.to_csv('1.csv',header=True,index=False)
    plt.plot(range(1,len(dateList)+1) , closePriceList)
    plt.title(f'{code}收盘价趋势图')

    plt.show()

stockinfo('cn_600009', '20180720', '20191020')
