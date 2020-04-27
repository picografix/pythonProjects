from math import sqrt
"""def isprime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True"""
def prime(n):
    for i in range(2,n+1):
        if i==n:
            return [i]
        elif n%i==0:
            return [i] + prime(n//i) 
def popins(li,n):
    to_pop = set(prime(n))
    li_set = set(li)
    ans_set = li_set - to_pop
    return len(ans_set)
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
