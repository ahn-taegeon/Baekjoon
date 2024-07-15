N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)
lst.sort()
for i in range(N):
    print(lst[i])