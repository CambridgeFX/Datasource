import bls
import pandas as pd


def blsdata(keyid,api):

    df = bls.get_series(keyid, 2011, 2020,key = api)
    df.to_excel('bls.xlsx')
    df = pd.read_excel('bls.xlsx')
    df.columns = ['date','value']
    return df
