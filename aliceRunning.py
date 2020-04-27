def rank(li,a):
    b= sorted(li,reverse=True)
    return b.index(a)+1
n = int(input())
marks =[]
no = []
data =[]
for i in range(n):
    arr = [int(x) for x in input().strip().split(' ') ]
    marks.append(int(arr[1]))
    no.append(arr[0])
    arr1 = [int(x) for x in input().strip().split(' ') ]
    data.append(arr1)
for i in range(n):
    print(rank(data[i],marks[i]))
