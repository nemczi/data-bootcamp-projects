# importing txt file in python as string?
file=open(r"C:\Users\iljin\Desktop\visual data analyt\ilp quest 1\nassa.txt")
# assignin opened file to variable. why? 
nassa_file=file.read()
nassa_file=nassa_file.lower()
# checking if thats correct /ok thats works commenting it out for now
# print(nassa_file)


# HOW TO GET IT IN EXCEL FILE??

# creating excel XLSV file imporing it in here and see its structure
# Method above didnt worked out. google says use panads or other libraries.
import pandas as pd
# print(pd.__version__)
# example_data_xlsv=pd.read_csv(r"C:\Users\iljin\Desktop\visual data analyt\ilp quest 1\example1.csv")
# # print(example_data_xlsv)
# # # structure of datafreme of example file
# # print(example_data_xlsv.info())
# # idea is to convert txt file to dataframe and then to csv


# lets clear a bit our string
# print(len(nassa_file))# total lenght
# print(nassa_file.rfind("year"))#where actual table finishes
# print(nassa_file.find("year"))#and where it starts should clear it a bit
# first_coment=nassa_file[0:406]
# last_comment=nassa_file[16583:]
dataf=nassa_file[406:16583]
#spliting whole text in 3 parts actual data table,header and coment section
# print(first_coment)
# print(last_comment)
# print(dataf.find("year "))
# print(dataf.find(" year"))
first_row=dataf[0:104]
# clearing more of what i think we dont need and imporin re in order to do it
import re
print(first_row.split())
first_row_list=(first_row.split())
print(len(first_row_list))
#actual cleaning
for i in first_row_list:
    dataf=re.sub(i,"",dataf)
    dataf=re.sub(" +"," ",dataf)
    dataf=re.sub(r'\n\s*\n', '\n',dataf, flags=re.MULTILINE)#not my

#how to get indexes for out data frame?
# assuming or index will be a year


# THIS DIDNT WORKED OUT
# for i in range(1880,2024):
#     a=str(i)
#     list_of_one_year=(re.findall(a,dataf))
#     list_of_one_year.pop()
#     list_year.extend(list_of_one_year)
# print(list_year)

#NEXT TRY
def year_finder_list(text):
    z=list("")
    for i in range(1880,2066):
        year_in_string=str(i)
        x=(re.findall(year_in_string,text))
        while len(x)>1:
            x.pop()
        
        z.extend(x)
    return(z)

    
        

# print (year_finder_list(dataf))
year_list=(year_finder_list(dataf))
df=pd.DataFrame(index=(year_finder_list(dataf)))
# print(df)

x=dataf.splitlines()#hmm thats my work
print(len(x))
print(x[1])
abc=x[1].split()
abc.pop(0)
abc.pop()
print(abc)
fff=pd.DataFrame(value=abc,index=(year_finder_list(dataf)))
print(fff)
    

#NOW WE NEED VALUES AND ITS TIME TO START CHOPING STRINGS FOR THEM
# print(dataf)

def choping_string_between_same_values(text):
    for i in range(1880,2066):
        year_in_string=str(i)

        

        
        print(x)

    
        

# choping_string_between_same_values(dataf)

