def identify(a,b,c):
    lst = [a,b,c]
    box = []
    for i in lst:
        box.append(lst.count(i)) 
    if sum(lst) != 180:
        return "Error"
    elif max(box) == 3:
        return "Equilateral"
    elif max(box) == 2:
        return "Isosceles"
    else:
        return "Scalene"

lst = []

a = int(input())
b = int(input())
c = int(input())

print(identify(a,b,c))