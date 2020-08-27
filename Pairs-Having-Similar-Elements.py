'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def countsimilar(N,arr):
    counter = 0
    n,k=1,1
    for i in range(N):
        try:
            if arr[i]==arr[i+1]-1:
                n+=1
            elif arr[i]==arr[i+1]:
                n+=1
                k+=1
            else:
                if n!=k :
                    counter += ((n)*(n-1)//2)
                n = 1
                k = 1
        except:
            if n!=k :
                    counter += ((n)*(n-1)//2)
            n = 1
            k = 1
    return counter

n = int(input())
a = list(map(int, input().rstrip().split()))
# a = [1, 3, 5, 7 ,8 ,2, 5, 7]
# n= 8
a = sorted(a)
count = countsimilar(n,a)
# print(a)
print(count)
