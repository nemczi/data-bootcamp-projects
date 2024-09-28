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
# print(datatable.find("year "))
# print(datatable.find(" year"))
first_row=datatable[datatable.find("year "):datatable.find(" year")+5]#getting column names
first_row=(first_row.split())#turnin them in to list
first_row.pop()# removing unwanted "year" at the end.
# print(first_row)
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
# print(len(data_rows))
# print(data_rows[1])

#Making lists of temperatures in one big list
temperature_list=[]
for i in range(0,len(data_rows)):
    abc=data_rows[i].split()
    if len(abc)>=1:
        abc.pop()#removing "year" from the end of the row
        temperature_list.append(abc)
#Still, I managed to make empty lists
#Trying to get rid of them
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
#That's where I realized that I didn't have to make a separate list of indexes
df.to_excel("ILP_task_final2.xlsx",index=False)


#line 3 how to make it usable for others?
#lines 9,10,11 probably should not slice string manualy like that
#line 16 tried different approach.looks awful and unreadable.
#line 28 and 45 I dont know how to make a list in loop without making empty list outside
#line 48 should use only lists that contains something,however empty list was still made and added dont know why.
#Comment writing is still an ssue
#naming variables in loops,dont look right for me.
#is it a good practice to keep "print" in code commented out in case to see what part of that code does?
