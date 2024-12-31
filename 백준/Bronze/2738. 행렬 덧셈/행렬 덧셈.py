N,M = map(int, input().split())

arr1 = []
for i in range(N):
    arr1.append(list(map(int, input().split())))
arr2 = []
for i in range(N):
    arr2.append(list(map(int, input().split())))
arr3 = [[arr1[i][j] + arr2[i][j] for j in range(M)] for i in range(N)]
for k in range(N):
    print(*arr3[k])