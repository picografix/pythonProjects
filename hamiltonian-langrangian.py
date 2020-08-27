'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
#function here
# def recursive(arr,count):
#     if length(arr)==1: 
#         return count
#     else :
#         if arr[-2] > count[0]:
#             count = [arr[-2]]+count
#         return recursive(arr[:-3],count)


# Write your code here
n = int(input())
a = list(map(int, input().rstrip().split()))
# for i in reversed(range(n)):
#     try:    
#         if a[i]>=max(a[i-1:]):
#             print(a[i],end=' ')
#     except:
#         print(a[i],end=' ')
count  = []
for i in reversed(range(n)):
    if i==n-1 :
        count= [a[i]]+count
    elif a[i] >= count[0]:
        count= [a[i]]+count
    else:
        continue
for i in count:
    print(i,end=' ')
