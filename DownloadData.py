import pandas as pd
from fredapi import Fred
filepath = "S:\CurrencyRiskAnalytics\PRESENTATIONS\FRED & OTHER DATA SOURCES\DataList.xlsx"
df = pd.read_excel(filepath)
file_name = "S:\CurrencyRiskAnalytics\PRESENTATIONS\FRED & OTHER DATA SOURCES\FRED Trial.xlsx"
fred = Fred(api_key="46b412ebf2535fc3addf5e27987aa6d6")
writer = pd.ExcelWriter(file_name, engine='xlsxwriter',datetime_format='mm/dd/yyyy')
for i,j in zip(df.iloc[:,0],df.iloc[:,1]):
    df_fred = pd.DataFrame()
    df_fred = fred.get_series(j)
    sheetname = i[0:30]
    df_fred.to_excel(writer,sheetname)
    workbook = writer.book
    worksheet = writer.sheets[sheetname]
    worksheet.write('A1','DATE')
    worksheet.write('B1', i)
    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({
        'categories': [sheetname, 1, 0, df_fred.shape[0], 0],
        'values': [sheetname, 1, 1, df_fred.shape[0], 1],
        'line': {'color': '#503B6B',
                 'width': 1.5,
                 },
    })
    chart.set_x_axis({
        'date_axis': True,
        'major_unit': 5,
        'major_unit_type': 'years',
        'num_format': 'yyyy',
        'num_font': {'name': 'Roboto Medium', 'size': 8},
        'line': {'color': '#BFBFBF'}
    })
    chart.set_y_axis({'visible': True,
                      'major_gridlines': {
                          'visible': True,
                          'line': {'width': 0.75, 'transparency': 80, 'color': '#BFBFBF'}, },
                      'line': {'color': '#FFFFFF'},
                      'num_font': {'name': 'Roboto Medium', 'size': 8}
                      })
    chart.set_legend({'none': True})
    worksheet.insert_chart('D2', chart, {'x_scale': 2, 'y_scale': 1.5})

writer.save()


