import re
def year_finder_list(text):
    for i in range(0,3000):
        Year_in_string=str(i)
        Year=re.search(Year_in_string,text)
        return Year
    
month_map={}