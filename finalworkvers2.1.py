import re
import pandas as pd
import numpy as np
import openpyxl
file=pd.read_fwf(r"GLB.Ts+dSST.txt",sep=" ",header=None)

#Cleaning from comments 
#removing no value lines,dont know why and how,but thats mostly is text comments.
#removing duplicates
#removing multiple white spaces
#removing column names and replacing them with first row of datatable
#re-indexing it all

df=pd.DataFrame(file)
df=df.dropna()
df.drop_duplicates(inplace=True)
df=df.replace(r"\s+"," ",regex=True)
df.columns=df.iloc[0]
df=df[1:]
df.reset_index(drop=True,inplace=True)


#Column from Jan to JJA went as single column instead of 17 columns
#so we taking that column out and spliting it in 17 columns
#doing it separetly with column names and values in table
#I have had dificulties to split values the right way,I had to use to_list method

colum_to_work_with=df[df.columns[1]]
column_values=colum_to_work_with.str.split()
column_name=colum_to_work_with.name
column_name=column_name.split()
column_values=(column_values.to_list())

#I am creating a dataframe below using the column above.
#The initional dataframe was split in parts and I split it in a way which can be recombined  
#in dataframe where we substitue single column with dataframe.
df2=pd.DataFrame(columns=column_name,data=column_values)
dfpart1=df.iloc[:,:1]
dfpart2=df.iloc[:,2:]
result=pd.concat([dfpart1,df2,dfpart2],axis=1)
result.to_excel("ILP_Pd_txt_to_excel.xlsx",index=False)
ss1=result.astype("Int64",errors="ignore")
print(ss1)
print(result.apply(np.isfinite))


