import re
import pandas as pd
import numpy as np
import openpyxl
file=pd.read_fwf(r"GLB.Ts+dSST.txt",sep=" ",header=None)

df=pd.DataFrame(file)
df=df.dropna()
df.drop_duplicates(inplace=True)
df=df.replace(r"\s+"," ",regex=True)
df.reset_index(drop=True,inplace=True)
df.columns=df.iloc[0]
df=df[1:]
df.reset_index(drop=True,inplace=True)
s1=df[df.columns[1]]
b=s1.str.split()

a=s1.name
a=a.split()
# print(a)
b=(b.to_list())
df2=pd.DataFrame(columns=a,data=b)
dfpart1=df.iloc[:,:1]
dfpart2=df.iloc[:,2:]
result=pd.concat([dfpart1,df2,dfpart2],axis=1)
print(result)


