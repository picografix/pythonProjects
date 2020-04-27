def check(li):
    a=len(li)
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
def seq(n):
    ans = [1,3,5]
    k = 4
    while k <= n:
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                a = ans[i]
                b = ans[j]
                temp = sorted(ans+[a+b])
                if check(temp):
                    ans = temp
                    break
                else:
                    continue
        k +=1            
    return sorted(ans)
print(seq(10))
        