a = map(int, input(). split())
list_a = list(a)
list_a[0] = 1 - list_a[0] 
list_a[1] = 1 - list_a[1]
list_a[2] = 2 - list_a[2]
list_a[3] = 2 - list_a[3]
list_a[4] = 2 - list_a[4] 
list_a[5] = 8 - list_a[5]
for i in list_a:
    print(i, end=" ")