Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> const=0
def min(arr):
    x=arr[0]
    global cosnt
    for y in arr:
        const+=1
        if(x>y):
            x=y
    return x

def orden(arr):
    aux=arr[:]
    arrsort=[]
    for x in range(len(aux)):
        y=min(aux)
        aux.remove(y)
        arrsort.append(y)
    return arrsort

import random
p=random.sample(range(0,100),25)
print(p)
psort=orden(p)
print(cnt)
print(psort)
