N = int(input())

end_int = N
times = 0
while True:
    times += 1
    if N < 10:
        N = N*10 + N
    else:
        n_1 = N // 10
        n_2 = N % 10
        N = 10 * n_2 + ((n_1+n_2)%10)
    
    if N == end_int:
        break

print(times)