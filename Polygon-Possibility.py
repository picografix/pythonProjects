n = int(input())
for _ in range(n):
    N = int(input())
    a = list(map(int, input().rstrip().split()))
    a = sorted(a)
    c = sum(a[:N-1])
    if a[-1] < c :
        print('Yes')
    else:
        print('No')
