N = int(input())
lst = [list(map(str,input().split())) for _ in range(N)]
dancing = set(["ChongChong"])

for sub_lst in lst:
    for s in sub_lst:
        if s in dancing:
            sub_lst.remove(s)
            dancing.add(sub_lst[0])
        

print(len(dancing))