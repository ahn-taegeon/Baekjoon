N = int(input())
def factorial(x):
    value = x
    result = 1
    while x > 0:
        result = result * x
        x = x - 1
    return result
print(factorial(N))