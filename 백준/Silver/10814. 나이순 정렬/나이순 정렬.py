N = int(input())
member = []
for i in range(N):
    age,name = map(str,input().split())
    member.append((int(age),name)) # 튜플로 리스트에 저장(나이를 int로 받아야함)
member.sort(key=lambda x : (x[0])) # 튜플의 0번째(나이)를 기준으로 정렬     
for k in member:
    print(k[0],k[1])
