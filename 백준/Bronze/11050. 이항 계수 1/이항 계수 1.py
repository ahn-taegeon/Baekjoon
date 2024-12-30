N,K = map(int, input().split())
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
print(int(combination(N,K)))