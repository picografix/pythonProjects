a=[1,2,3,2,5]
x=4
 
def check(a,x):
    n=len(a)
    c=0
    i=0
    while(i<(n)):
        for j in range(i+1,n):
            if ((a[i]+a[j])==(x)):
                c=c+1
        i=i+1
    return c
print(check(a,x))