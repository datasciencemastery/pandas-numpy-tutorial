import pandas as pd


df = pd.read_csv('pandas_data_sheet.csv',sep = ',')
df = pd.read_csv('https://raw.githubusercontent.com/datasciencemastery/data-sets/master/data_sheet.csv',sep = ',', error_bad_lines=False)

print(df)
