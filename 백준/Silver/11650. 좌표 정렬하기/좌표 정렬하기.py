N = int(input())
lst = []
for _ in range(N):
    p = list(map(int, input().split()))
    lst.append(p)
lst.sort()
for i in lst:
    print(*i)