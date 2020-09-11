a=[0,-1,2,-3,1] 
def triplet(a):
    n=len(a)
    p=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i]+a[j]+a[k]==0 :
                    p.append([a[(i)],a[j],a[k]])   
    return p
print(triplet(a))