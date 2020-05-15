
#FRED

keyid = "GDPC1"
api = "46b412ebf2535fc3addf5e27987aa6d6"
df = freddata(keyid,api)
df.to_json('GDPC1.json',orient='records',date_format='iso')
#BLS

api = '35a12ce271ce4db9afb327051cb675a8'
keyid = 'CUUR0000SA0'
df = blsdata(keyid,api)
# we need add starting point and end point in it.
#StatsCan
import pandas as pd
from StatsCan import *
#Employment
keyid = "2062811"
s = '1976-01-01T08:30'
e = '2020-05-08T19:00'
df = statscandata(keyid,s,e)
df.to_excel(VectorID + "2.xlsx")

#For change, you can try this:
#df["value"]=df['value']*df['value'].pct_change()

#Unemployment Rate
VectorID = "2062815"
StartDate = "1976-01-01T08:30"
EndDate = "2020-05-08T19:00"
df = pd.DataFrame.from_dict(SeriesData(VectorID,StartDate,EndDate))
df.to_excel(VectorID + ".xlsx")

df = pd.read_excel("20628112.xlsx",sheet_name="Sheet1")
df.to_json('Employment.json',date_format = 'iso',orient = 'records')

df = pd.read_excel("20628112.xlsx",sheet_name="Sheet2")
df.to_json('EmploymentChange.json',date_format = 'iso',orient = 'records')

df = pd.read_excel("20628152.xlsx",sheet_name="Sheet1")
df.to_json('UnemploymentRate.json',date_format = 'iso',orient = 'records')


df = pd.read_excel("20628152.xlsx",sheet_name="Sheet2")
df.to_json('UnemploymentRateChange.json',date_format = 'iso',orient = 'records')




import requests
import pandas as pd
url ='https://www150.statcan.gc.ca/t1/wds/rest/getBulkVectorDataByRange'
payload = {
  "vectorIds": ["2062811"],
  "startDataPointReleaseDate": "1985-10-01T08:30",
  "endDataPointReleaseDate": "2020-05-06T19:00"
}
r = requests.post(url=url,json=payload)
vector_data = r.json()[0]['object']
datapoint = vector_data.get("vectorDataPoint")
date_list = []
value_list = []
for i in datapoint:
    date_list.append(i['refPer'])
    value_list.append(i['value'])
datafordf = {'Date':date_list,'Value':value_list}
df = pd.DataFrame.from_dict(datafordf)


filepath = "S:\CurrencyRiskAnalytics\PRESENTATIONS\FRED & OTHER DATA SOURCES\DataList.xlsx"
df = pd.read_excel(filepath)
file_name = "FRED Trial.xlsx"
fred = Fred(api_key="46b412ebf2535fc3addf5e27987aa6d6")