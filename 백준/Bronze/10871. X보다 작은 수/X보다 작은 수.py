n, x = map(int, input(). split())
a = list(map(int, input(). split()))
b = []
for i in range(n):
    if a[i] < x:
        b.append(a[i])
for j in b:
    print(j, end=' ')