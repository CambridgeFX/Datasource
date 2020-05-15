from fredgrab import *
from blsgrab import *
from statscangrab import *

df_list = pd.read_excel('grabdatalist.xlsx')
for i in range(3,len(df_list['Source'])):
    print("Getting "+ df_list.iloc[i,1] +" data!")
    if df_list.iloc[i,0] == "FRED":
        keyid = df_list.iloc[i,2]
        api = df_list.iloc[i,3]
        df = freddata(keyid,api)
        df.to_json(df_list.iloc[i,4]+".json", orient='records', date_format='iso')
    elif df_list.iloc[i,0] == "BLS":
        keyid = df_list.iloc[i, 2]
        api = df_list.iloc[i, 3]
        s = int(df_list.iloc[i, 5])
        e = int(df_list.iloc[i, 6])
        df = blsseries(keyid, api, s, e)
        df.to_json(df_list.iloc[i,4]+".json", orient='records', date_format='iso')
    elif df_list.iloc[i,0] == "STATSCAN":
        keyid = df_list.iloc[i, 2]
        s = df_list.iloc[i, 5]
        e = df_list.iloc[i, 6]
        df = statscanseries(keyid, s, e)
        df.to_json(df_list.iloc[i,4]+".json", orient='records', date_format='iso')

