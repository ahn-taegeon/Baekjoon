S = input()
time = 0
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in alpha:
    if i in S:
        time += S.count(i)
        S = S.replace(i,'*')
time += len(S.replace('*',''))
print(time)