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

N = int(input())
num = list(map(int, input().split()))
num_prime = 0

for j in num:
    if det_prime(j):
        num_prime += 1
        
print(num_prime)