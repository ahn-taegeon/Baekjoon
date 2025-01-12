def identify(a,b):
    if b%a == 0:
        return "factor"
    elif a%b == 0:
        return "multiple"
    else:
        return "neither"
lst = []

while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    lst.append(identify(a,b))
for i in lst:
    print(i)