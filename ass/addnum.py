import re

def add(x):
   
    array = (re.findall(r'[-+]\d+', x))
    for i in array:
     if(i.lstrip('-').isdigit()):
         return "negatives not allowed "+ i
    
    temp = re.findall(r'\d+', x)
    res = list(map(int, temp))
    sum = 0
    for i in res:
     sum = sum + i 
    return sum  
    