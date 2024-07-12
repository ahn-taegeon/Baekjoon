S = input().lower()
set_S = set(S)
max = 0
for i in set_S:
    if S.count(i) > max:
        max = S.count(i)
        a = i
    elif S.count(i) == max:
        a = "?"
print(a.upper())