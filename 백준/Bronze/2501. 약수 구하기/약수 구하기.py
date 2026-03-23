N, K = map(int, input().split())

lst = []

for i in range(1,N+1):
    if N%i == 0 & (not i in lst):
        lst.append(i)
lst.sort()

if len(lst) < K:
    print(0)
else:
    print(lst[K-1])