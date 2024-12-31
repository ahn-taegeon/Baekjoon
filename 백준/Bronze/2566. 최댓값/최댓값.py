arr= []
lst = []
row = 0
column = 0
for _ in range(9):
    arr.append(list(map(int, input().split())))
for i in range(9):
    lst.append(max(arr[i]))
max_value = max(lst)
for i in range(9):
    if max_value in arr[i]:
        row = i+1
        column = 1+arr[i].index(max_value)
print(max_value)
print(row, column)