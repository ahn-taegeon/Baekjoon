N = int(input())
count = 0
for _ in range(N):
    s = input()
    length = int(len(s))
    lst = []
    for i in range(length):
        if i == length-1:
            lst.append(s[i])
        elif s[i] == s[i+1]:
            pass
        elif s[i] != s[i+1]:
            lst.append(s[i])
    if len(lst) == len(set(lst)):
        count += 1
    else:
        pass
print(count)