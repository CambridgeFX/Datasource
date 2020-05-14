from fredapi import Fred


def freddata(keyid, api):

    fred = Fred(api_key=api)
    df = fred.get_series(keyid)
    df = df.to_frame().reset_index()
    df.columns = ['date', 'value']
    return df

