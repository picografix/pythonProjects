from math import sqrt
def summation(f,a,b,n):
    sum=0
    for i in range(a,b+1):
        if i > sqrt(n):
            break
        else:
            sum += f(n,i)    
    sum += (b-i + 1)*n
    return (sum%(1000000007))

def fun(n,i):
    
    a = n%(i**2)
    return a
if __name__=="__main__":
    cases = int(input())
    n=[]
    m=[]
    for i in range(cases):
        arr = input().split(' ')
        arr=[int(i)  for i in arr]
        n.append(arr[0])
        m.append(arr[1])
        
    for i in range(cases):
        an = summation(fun,1,m[i],n[i])
        print(an)
    