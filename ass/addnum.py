import re

def add(x):
    temp = re.findall(r'\d+', x)
    res = list(map(int, temp))
    sum = 0
    for i in res:
        sum = sum + i
    return sum
