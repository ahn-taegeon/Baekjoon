N,M = map(int,input().split())
basket = []
for i in range(N):
    basket.append(str(i+1))
for i in range(M):
    a,b = map(int,input().split())
    basket[a-1],basket[b-1] = basket[b-1],basket[a-1]
result = " ".join(basket)
print(result)