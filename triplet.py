def dupli(a):
    for i in a :
        if a.count(i)>1:
            a.pop(a.index(i))
    return a
"""def suma(a):
    suma1=0
    for i in a:
        suma1 += i
    return suma1"""
n = int(input())
arr = input().split(' ')
arr = [int(i) for i in arr ]
ans= []
for i in arr:
    for j in arr[1:]:
        for k in arr[2:]:
            if i + j + k ==0 and i!=j and j!=k and i!=k:
                ans.append([i,j,k])
ans_sort=[]
for i in ans:
    lol = sorted(i)
    if ans_sort.count(lol)==0:
        ans_sort.append(lol)

if len(ans)==0:
    print(-1)
else:
    for i in ans_sort :
        print(i[0],i[1],i[2])