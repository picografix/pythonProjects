def dotpro(arr1,arr2,n):
    a=[]
    for i in range(n):
        b = arr1[i]*arr2[i]
        a.append(b)
    return a
def promatrices(arr1,arr2,n):
    arr=[0]*n*n
    for k in range(n):
        for i in range(k,n):
            s=0
            for j in range(n):
                a=i+n*j
                b=n*i+j 
                s+=arr1[a]*arr2[b]
            arr[i*k]+=s
    return arr
n = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
print(promatrices(a,b,n))