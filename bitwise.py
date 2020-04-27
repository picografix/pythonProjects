def check(li):
    for i in li:
        if li.count(i)>1:
            return True
    return False
def apply_and(a,b):
    return a&b

def apply(li,n,a):
    tryNo = 0
    while tryNo < n:
        for i in range(tryNo,n):
            temp = apply_and(li[i],a)
            if li.count(temp) >=1:
                return tryNo+1
        li[tryNo]=apply_and(li[tryNo],a)
        tryNo +=1
    return -1             
i = int(input())
for  n in range(i):
    arr_a = [int(i) for i in input().strip().split(' ')]
    arr_b = [int(i) for i in input().strip().split(' ')]
    if check(arr_b):
        print(0)
    else:
        print(apply(arr_b,arr_a[0],arr_a[1]))