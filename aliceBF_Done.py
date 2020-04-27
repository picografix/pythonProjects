def pairs(li,n):
    diff = 10000000000000000 
    a,b=0,0
    for i in range(n-1):
        j = i+1
        if i!=j and abs(li[i]-li[j]) < diff:
                diff = abs(li[i]-li[j])
                a = li[i]
                b = li[j]
        elif i!=j and abs(li[i]-li[j]) == diff and (a > li[i] or b > li[i]):
                a = li[i]
                b = li[j]
    return a,b
i = int(input())
for  n in range(i):
    a = input().strip()
    arr = [int(i) for i in input().strip().split(' ')]
    p,q = pairs(arr,int(a))
    print(min(p,q),max(p,q))