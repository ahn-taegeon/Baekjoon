N,M = map(int,input().split())
basket = []
for i in range(N):
    basket.append(str(i+1))
for _ in range(M):
    a,b = map(int,input().split())
    while True:
        if a >= b :
            break
        basket[a-1],basket[b-1]=basket[b-1],basket[a-1]
        a += 1
        b -= 1
result = " ".join(basket)
print(result)