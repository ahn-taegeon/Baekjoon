lst = []
sum = 0
N,K = map(int,input().split())
for i in range(N):
    a = int(input())
    lst.append(a)
lst.sort(reverse=True)
for i in range(N):
    if lst[i] > K:
        pass
    else:
        sum += K // lst[i]
        K = K % lst[i]
    if K == 0:
        break
print(sum)