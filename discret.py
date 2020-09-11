from math import sin,pi
def f(x):
    return sin(x)
def find_integral(arr,h):
    integral=0
    for i in range(len(arr)-1):
        # print("printing")
        integral += (1/2)*(h)*(f(arr[i])+f(arr[i+1]))
    return integral
arr=[]
n=10000
for i in range(1,n):
    arr.append(i*pi/n)
h= pi/n
print(find_integral(arr,h))