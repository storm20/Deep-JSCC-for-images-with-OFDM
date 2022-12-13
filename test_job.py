import pandas as pd
a = pd.read_csv('data1.csv') 
print(a) 
a = a.dropna()
print(a)
a = a.sort_values(by=['AM_BF_Dephasing'],ascending=False)
print(a)

a = a.round(2)
a.to_csv('data2.csv',index=False)