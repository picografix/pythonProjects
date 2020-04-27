from math import sqrt
def isprime(n):
    ans = True
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            ans = False
            break
        """if ans:
            li.append(n)"""
    return ans   

def divisors(n):
    count=1
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0 :
            if n//i == i and not isprime(i):
                count +=1
            elif n//i != i:
                if not isprime(i):
                    count+=2
                elif not isprime(n//i):
                    count+=1
    if not isprime(n):
            count+=1
    return count
i= int(input())
for j in range(i):
    n=int(input())
    print(divisors(n))
