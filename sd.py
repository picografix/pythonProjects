from random import random
x = []
for i in range(10):
    x.append(random()/10000000)

def sumof(arr):
    sum=0
    for i in arr:
        sum += i 
    return sum
def meanof(x):
    return sumof(x)/(len(x))
def standard_deviation(x):
    mean = meanof(x)
    sd=0
    for i in x:
        sd += (mean-i)**2
    return sd/len(x)
def standard_deviation2(x):
    mean = meanof(x)
    sd=0
    for i in x:
        sd += (i**2-mean**2)
    return sd/len(x)
print(x)
print(standard_deviation(x)*10**16,"            This is one")
print(standard_deviation2(x)*10**16,"           This is second")