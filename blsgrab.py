import bls
import pandas as pd

def blsseries(keyid, api, start, end):

    df = bls.get_series(keyid, start, end, api)
    df.to_excel('bls.xlsx')
    df = pd.read_excel('bls.xlsx')
    df.columns = ['date','value']
    return df
