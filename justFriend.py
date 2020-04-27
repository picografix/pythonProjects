def pairs(li,n):
    diff = 100000000 
    a,b=0,0
    for i in range(n):
        for j in range(i,n):
            if i!=j and abs(li[i]-li[j]) < diff:
                diff = abs(li[i]-li[j])
                a = min(li[i],li[j])
                b=max(li[i],li[j])
            elif i!=j and abs(li[i]-li[j]) == diff:
                a = min(li[i],a)
                b = min(li[j],b)
    return a,b
i = int(input())
for  n in range(i):
    a = input().strip()
    arr = [int(i) for i in input().strip().split(' ')]
    
for i in range(int(a)):    
    p,q = pairs(arr,int(a))
    print(p,q)