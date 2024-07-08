import random
lst = []
height = 0
T = True
for _ in range(9):
    a = input()
    lst.append(int(a))
while T:
    lst_1 = random.sample(lst,7)
    for i in lst_1:
        height += i
    if height == 100:
        T = False
    else:
        height = 0
sorted_lst = sorted(lst_1)
for j in sorted_lst:
    print(j)