from fredapi import Fred
import pandas as pd
fred = Fred(api_key="46b412ebf2535fc3addf5e27987aa6d6")
df = pd.DataFrame()
df = fred.get_series('FEDFUNDS')
file_name = "S:\CurrencyRiskAnalytics\PRESENTATIONS\FRED & OTHER DATA SOURCES\JSONTrial.xlsx"
sheetname = "FEDFUNDS"
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheetname)
df.shape[0]
workbook  = writer.book
worksheet = writer.sheets[sheetname]
chart = workbook.add_chart({'type': 'line'})
chart.add_series({
    'categories': [sheetname,0,0,df.shape[0],0],
    'values': [sheetname,0,1,df.shape[0],1],
    'line': {'color':'#503B6B',
             'width':1.5,
             },
})
chart.set_x_axis({
    'date_axis':       True,
    'major_unit':      5,
    'major_unit_type': 'years',
    'num_format':      'yyyy',
    'num_font':{'name':'Roboto Medium','size':8},
    'line':{'color':'#BFBFBF'}
})
chart.set_y_axis({'visible':True,
                  'major_gridlines': {
                      'visible': True,
                      'line': {'width': 0.75, 'transparency':80,'color':'#BFBFBF'},},
                  'line':{'color':'#FFFFFF'},
                  'num_font':{'name':'Roboto Medium','size':8}
})
chart.set_legend({'none': True})

worksheet.insert_chart('D2', chart,{'x_scale': 2, 'y_scale': 1.5})
workbook.close()
writer.save()

