def identify(a,b,c):
    lst = [a,b,c]
    box = []
    for i in lst:
        box.append(lst.count(i)) 
    if max(lst) >= sum(lst)-max(lst):
        return "Invalid"
    elif max(box) == 3:
        return "Equilateral"
    elif max(box) == 2:
        return "Isosceles"
    else:
        return "Scalene"

lst = []

while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    lst.append(identify(a,b,c))
for i in lst:
    print(i)