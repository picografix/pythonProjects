def check(li):
    a = len(li)
    ans=True
    sum = 0
    for i in range(a):
        for j in range(i,a):
            if i!=j and li[i]+li[j] !=sum:
                sum = li[i]+li[j]
            elif i!=j and li[i]+li[j] ==sum:
                ans = False
                break
    return ans
def term(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            a = li[i]
            b= li[j]
            temp = sorted(li+[a+b])
            if check(temp):
                li = temp
                return li
i = int(input())
ans = [1,3,4]
for n in range(i-3):
    ans = term(ans)
if len(ans)==i:
    print(ans)
else:
    print(-1)