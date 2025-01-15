def det_prime(n):
    count = 0
    if n == 2:
        return True
    elif n == 1:
        return False
    elif n % 2 == 0:
        return False
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False

M = int(input())
N = int(input())

num = [x for x in range(M,N+1)]
num_prime = 0
box = []

for j in num:
    if det_prime(j):
        box.append(j)

if len(box) == 0:
    print(-1)
else:        
    print(sum(box))
    print(min(box))