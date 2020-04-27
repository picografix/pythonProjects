def check(li):
    a = len(li)
    ans=True
    sum = 0
    for i in range(a-1):
        j = -1
        if li[i]+li[j] !=sum and sum != li[j]:
            sum = li[i]+li[j]
        elif li[i]+li[j] ==sum:
            ans = False
            break
    return ans
def seq(n):
    init = [1,3]
    i = 4
    while i <= 40000000:
        if len(init) < n:
            if check(init+[i]):
                init = init+[i]
                i+=1
            else:
                i +=1
        else:
            return init
n = int(input())
ans = seq(n)
if len(ans)==n:
    for i in range(n):
        print(ans[i],end=" ")
else:
    print(-1)
