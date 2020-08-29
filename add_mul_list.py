def add(a,b,N):
    lb=len(b)
    # print(b)
    if lb!=N:
        b = [0]*(N-lb)+b 
    ans= [0]*N
    for i in range(N):
        if i!=N-1:
            ans[i]=(a[i]+b[i])%10 + (a[(i+1)]+b[(i+1)])//10 
        elif i==N-1:
            ans[i]=(a[i]+b[i])%10
    if (a[0]+b[0])//10>0:
        ans = [(a[0]+b[0])//10]+ans
    return ans
def mul(a,b,N):
    ar =[0]*N
    for i in range(N):
        ar[i] = [b[i]*element for element in a]+[0]*(N-1-i)
    a = [0]*(len((ar[0])))
    for j in ar:
        a = add(a,j,len(a))        
    print(ar)
    return a


N = int(input())
a = [int(i) for i in input()]
b = [int(j) for j in input()]
# print(a)
# print(b)
print(add(a,b,N))
print(mul(a,b,N))
