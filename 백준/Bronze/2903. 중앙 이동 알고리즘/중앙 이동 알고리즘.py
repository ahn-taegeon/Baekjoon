N = int(input())

n = 1
a_n = 3
while n < N:
    n += 1
    a_n = 2*a_n - 1
print(a_n ** 2)