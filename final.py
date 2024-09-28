import re
import pandas as pd
file=open(r"C:\Users\iljin\Desktop\visual data analyt\ilp quest 1\nassa.txt")
nassa_file=file.read()
nassa_file=nassa_file.lower()
# print(len(nassa_file))# total lenght
# print(nassa_file.rfind("year"))#where actual table finishes
# print(nassa_file.find("year"))#and where it starts
first_coment=nassa_file[0:406]#first comment
last_comment=nassa_file[16583:]#last comment
datatable=nassa_file[406:16583]#actual data

#COLUMN NAME EXTRCACTION
# print(datatable.find("year "))
# print(datatable.find(" year"))
first_row=datatable[datatable.find("year "):datatable.find(" year")+5]#getting column names
first_row=(first_row.split())#turnin them in to list
first_row.pop(0)
first_row.pop()

#REMOVING COLUM NAMES,EMPTYLINES AND MULTIPLEWHITESPACES FROM DATA TABLE
for i in first_row:
    datatable=re.sub(i,"",datatable)
    datatable=re.sub(" +"," ",datatable)
    datatable=re.sub(r'\n\s*\n', '\n',datatable, flags=re.MULTILINE)#not my
# print(datatable)
#INDEX EXTRCATION(YEARS) FUNCTION
def year_finder_list(firstyear,lastyear,text):
    z=list("")
    for i in range(firstyear,lastyear):
        year_in_string=str(i)
        x=(re.findall(year_in_string,text))
        while len(x)>1:
            x.pop()
        
        z.extend(x)
    return(z)
list_of_years=(year_finder_list(1700,2300,datatable))

#Getting list of temperature  values 
data_rows=datatable.splitlines()
# print(len(data_rows))
# print(data_rows[1])
temperature_list=[]
for i in range(0,len(data_rows)):
    abc=data_rows[i].split()
    if len(abc)>=1:
        abc.pop(0)
        abc.pop()
        temperature_list.append(abc)
i=0    
while i<=len(temperature_list):
    print(len(temperature_list))
    if len(temperature_list[i])==0:
        del temperature_list[i]
        if i==(len(temperature_list)):
            break
    else:
        i+=1

df=pd.DataFrame(index=list_of_years,data=temperature_list,columns=first_row,)
print(df)

df.to_csv("I did it3.csv",index=True)