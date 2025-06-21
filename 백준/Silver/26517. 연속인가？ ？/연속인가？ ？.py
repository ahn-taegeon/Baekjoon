k = int(input())
a,b,c,d = map(int,input().split())

if a*k+b == c*k+d:
    value = a*k+b
    print("Yes",value)
else:
    print("No")