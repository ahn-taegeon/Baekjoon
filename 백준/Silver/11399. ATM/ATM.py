N = int(input())
time = list(map(int, input().split()))
time.sort()
summation = time[0]
for i in range(1,len(time)):
    part = time[:i+1]
    summation += sum(part)
print(summation)