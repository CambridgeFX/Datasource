import requests
import pandas as pd


def statscanseries(keyid,start,end):

    url = 'https://www150.statcan.gc.ca/t1/wds/rest/getBulkVectorDataByRange'
    payload = {
      "vectorIds": [keyid],
      "startDataPointReleaseDate": start,
      "endDataPointReleaseDate": end
    }
    r = requests.post(url=url,json=payload)
    vector_data = r.json()[0]['object']
    datapoint = vector_data.get("vectorDataPoint")
    date_list = []
    value_list = []
    for i in datapoint:
        date_list.append(i['refPer'])
        value_list.append(i['value'])
    datafordf = {'date':date_list,'value':value_list}
    df = pd.DataFrame.from_dict(datafordf)
    return df

