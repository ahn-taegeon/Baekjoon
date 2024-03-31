a = int(input())
for i in range(a):
    m, d = input(). split()
    for j in d:
        print(j*int(m), end='')
    print()