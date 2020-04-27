def sumof(li):
    sum=0
    for i in li:
        sum += i
    return sum
def subseq(li,a):
    count = 0  
    if sumof(li)%2==1:
        return -1
    else:
        for i in range(a):
            if sumof(li[0:i])%2 ==0:
                count +=1
                li = li[i:]
            else:
                continue
        return count        

i = int(input())
for  n in range(i):
    a = int(input())
    arr = [int(i) for i in input().strip().split(' ')]
    print(subseq(arr,a))