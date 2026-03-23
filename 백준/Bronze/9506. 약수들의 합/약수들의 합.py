n_lst = []

while True:

    n = int(input())
    if n == -1:
        break
    n_lst.append(n)

measure = []


for N in n_lst:
    N_measure = []
    for i in range(1,N):
        if N%i == 0 & (not i in N_measure):
            N_measure.append(i)
    N_measure.sort()
    measure.append(N_measure)

for i, n_measure in enumerate(measure):

    n = n_lst[i]
    if n == sum(n_measure):
        summation = ' + '.join(map(str, n_measure))
        print(f"{n} = {summation}")
    else:
        print(f"{n} is NOT perfect.")