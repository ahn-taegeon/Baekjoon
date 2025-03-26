N = input()
length = len(N)
lst = [int(x) for x in N]
lst.sort(reverse=True)
for i in lst:
    print(i,end='')