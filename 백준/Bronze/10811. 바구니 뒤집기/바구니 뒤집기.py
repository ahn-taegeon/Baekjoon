N,M = map(int,input().split())
basket = []
for i in range(N): # 바구니 번호 지정
    basket.append(str(i+1))
for _ in range(M):
    a,b = map(int,input().split()) # 뒤집을 바구니 범위
    while True:
        if a >= b : # 범위 중간을 지나가면 중단
            break
        basket[a-1],basket[b-1]=basket[b-1],basket[a-1] # 범위 양끝에서 하나씩 뒤집기
        a += 1
        b -= 1
result = " ".join(basket)
print(result)
