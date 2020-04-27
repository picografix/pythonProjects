from math import sqrt
from random import randint
def isprime(n) : 
  
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
  
    return True 
"""def popins(li):
    for i in li[1:]:
        if isprime(i):
            li.pop(li.index(i))
    return len(li)"""
def divisors(n) : 
    div =[] 
    # Note that this loop runs till square root 
    i = 1
    while i <= sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n / i == i) : 
                if not isprime(i):
                    div.append(i) 
            else : 
                # Otherwise print both 
                if not isprime(i):
                    div.append(i)    
                if not isprime(n/i):
                    div.append(n/i) 
        i = i + 1
    return div
i= int(input())
for j in range(i):
    n=int(input())
    print(len(divisors(n)))
for k in range(2000):
    
