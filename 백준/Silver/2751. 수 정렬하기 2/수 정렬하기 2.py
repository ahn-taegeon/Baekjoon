import sys
N = int(input())
lst = []
for _ in range(N):
    n = int(sys.stdin.readline())
    lst.append(n)
lst.sort()
for i in lst:
    print(i)