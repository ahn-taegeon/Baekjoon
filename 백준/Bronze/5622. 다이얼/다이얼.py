ST = input()
length = len(ST)
time = 0
for i in range(len(ST)):
    if ST[i] in ['A','B','C']:
        time += 3
    elif ST[i] in ['D','E','F']:
        time += 4
    elif ST[i] in ['G','H','I']:
        time += 5
    elif ST[i] in ['J','K','L']:
        time += 6
    elif ST[i] in ['M','N','O']:
        time += 7
    elif ST[i] in ['P','Q','R','S']:
        time += 8
    elif ST[i] in ['T','U','V']:
        time += 9
    elif ST[i] in ['W','X','Y','Z']:
        time += 10
print(time)