lst = []
lst_sep = []
for _ in range(5):
    lst.append(input())
max_len = max([len(x) for x in lst])
for j in range(max_len): 
    for i in range(5):
        try:
            lst_sep.append(lst[i][j])
        except IndexError:
            pass
print(*lst_sep, sep="")