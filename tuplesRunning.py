def maxima(li):
    return li[-1]
def minima(li):
    return li[0]
def test(arr_a,arr_b):
    arr_a.sort()
    arr_b.sort()
    if maxima(arr_a) < minima(arr_b):
        return "Nice"
    elif maxima(arr_b) < minima(arr_a):
        return "Nice"
    else:
        return "Not nice" 

i = int(input())
for  n in range(i):
    a = int(input())
    arr_a = [int(i) for i in input().strip().split(' ')]
    arr_b = [int(i) for i in input().strip().split(' ')]
    print(test(arr_a,arr_b))