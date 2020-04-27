from math import sqrt
def prime(n):
    for i in range(2,n+1):
        if i==n:
            return [i]
        elif n%i==0:
            return [i] + prime(n//i)
def popins(li,n):
    oho = prime(n)
    for i in oho:
        if i in li:
            li.pop(li.index(i))
    return len(li)
def divisors(n) : 
    div =[] 
    # Note that this loop runs till square root 
    i = 1
    while i <= sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n / i == i) : 
                div.append(i) 
            else : 
                # Otherwise print both 
                div.append(i) 
                div.append(n/i) 
        i = i + 1
    return div
i= int(input())
for j in range(i):
    n=int(input())
    print(popins(divisors(n),n))
