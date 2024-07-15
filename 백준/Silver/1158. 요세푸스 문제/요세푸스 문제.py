N,K = map(int,input().split())
circle = []
result = []
for i in range(N):
    circle.append(i+1)
add = 0
for j in range(N):
    add = (add + K - 1) % len(circle)
    result.append(str(circle.pop(add)))
answer = ", ".join(result)
print('<' + answer + '>')