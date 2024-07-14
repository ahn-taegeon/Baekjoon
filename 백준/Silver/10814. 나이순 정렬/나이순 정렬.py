N = int(input())
member = []
for i in range(N):
    age,name = map(str,input().split())
    member.append((int(age),name))
member.sort(key=lambda x : (x[0]))    
for k in member:
    print(k[0],k[1])