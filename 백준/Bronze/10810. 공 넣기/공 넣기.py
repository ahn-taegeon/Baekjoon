N,M = map(int,input().split())
basket = []
for _ in range(N):
    basket.append('0')
for _ in range(M):
    a,b,c = map(int,input().split())
    for i in range(a-1,b):
        basket[i] = str(c)
result = " ".join(basket)
print(result)