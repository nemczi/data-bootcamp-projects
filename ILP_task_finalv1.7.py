import re
import pandas as pd
import openpyxl
file=open(r"GLB.Ts+dSST.txt")
nassa_file=file.read()
nassa_file=nassa_file.lower()
# print(len(nassa_file))# total lenght
# print(nassa_file.rfind("year"))#where actual table finishes
# print(nassa_file.find("year"))#and where it starts
first_coment=nassa_file[0:406]#first comment
last_comment=nassa_file[16583:]#last comment
datatable=nassa_file[406:16583]#actual table with data

#COLUMN NAME EXTRCACTION

first_row=datatable[datatable.find("year "):datatable.find(" year")+5]#getting column names +5 becouse we want " year" to be included
first_row=(first_row.split())#turnin them in to list
first_row.pop()# removing unwanted "year" at the end.


#REMOVING COLUM NAMES,EMPTYLINES AND MULTIPLEWHITESPACES FROM DATA TABLE
for i in first_row:
    datatable=re.sub(i,"",datatable)
    datatable=re.sub(" +"," ",datatable)
    datatable=re.sub(r'\n\s*\n', '\n',datatable, flags=re.MULTILINE)#not my,thats why I probably got empty list
# But I got idea of that.


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


#Making lists of temperatures in one big list
temperature_list=[]
for i in range(0,len(data_rows)):
    abc=data_rows[i].split()
    if len(abc)>=1:
        abc.pop()#removing "year" from the end of the row
        temperature_list.append(abc)
#Still, I managed to make empty lists


#Trying to get rid of empty lists with while loop for lists that are 0 long and deleting them
i=0    
while i<len(temperature_list):
    # print(len(temperature_list))
    if len(temperature_list[i])==0:
        del temperature_list[i]
        if i==(len(temperature_list)):
            break
    else:
        i+=1



#Putting it all together
df=pd.DataFrame(index=list_of_years,data=temperature_list,columns=first_row)
print(df)
# where I realized that I didn't have to make a separate list of indexes
df.to_excel("ILP_task_finalv18.xlsx",index=False)
print(df)

