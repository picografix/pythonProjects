import matplotlib.pyplot as plt
from math import exp
def f(n):
    if n==0:
        return 1-(1/exp(1))
    else:
        return 1-n*f(n-1)
a=[]
b=[]
for i in range(20):
    a.append(i+1)
    b.append(f(i))
    #print(f(i))
plt.plot(a,b,'ro')
plt.plot(a,b)
plt.ylabel('some numbers')
plt.show()