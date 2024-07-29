lst = []
result = []

N = int(input())
for _ in range(N):
    S = input()
    if 'push' in S:
        j = S.split()
        lst.append(int(j[-1]))
    elif S == 'size':
        result.append(len(lst))
    elif S == 'empty':
        if len(lst) == 0:
            result.append(1)
        else:
            result.append(0)
    elif S == 'pop':
        if len(lst) == 0:
            result.append(-1)
        else:
            t = lst.pop(0)
            result.append(t)
    elif S == 'back':
        if len(lst) == 0:
            result.append(-1)
        else:
            result.append(lst[-1])
    elif S == 'front':
        if len(lst) == 0:
            result.append(-1)
        else:
            result.append(lst[0])
for i in range(len(result)):
    print(result[i])
