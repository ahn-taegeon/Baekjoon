N = int(input())
star = '*'
for i in range(1,N+1):
    stars = star * (2*i-1)
    print(stars.center(2*N-1, ' ').rstrip())
for i in range(N-1,0,-1):
    stars = star * (2*i-1)
    print(stars.center(2*N-1, ' ').rstrip())