import pandas as pd
df = pd.read_csv('/home/xand/Desktop/Xattendance/Data/s03_pds.csv')
series = pd.Series(['Hello', 'Bye', 'Hello', 'fgb'], index = ['Unnamed: 0','1','O170939','UMMADI SANITHA'])
print(series)
df.iloc[2] = series
print(df)
