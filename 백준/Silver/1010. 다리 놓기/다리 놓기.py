T = int(input())
lst = []
def factorial(x):
    value = x
    result = 1
    while x > 0:
        result = result * x
        x = x - 1
    return result
def combination(N,K):
    if N < K:
        result = 0
    else:
        result = factorial(N)/(factorial(N-K)*factorial(K))
    return result
for _ in range(T):
    K,N = map(int, input().split())
    lst.append(int(combination(N,K)))
for value in lst:
    print(value)