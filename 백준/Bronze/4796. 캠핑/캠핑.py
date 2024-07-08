T = True
lst = []
while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    case_1_m = c//b
    case_1_n = c%b
    if case_1_n > a:
        case_1 = a*case_1_m + a
    else:
        case_1 = a*case_1_m + case_1_n
    lst.append(case_1)
num = len(lst)
for i in range(1,num+1):
    print(f"Case {i}: {lst[i-1]}")