a, b = map(str,input(). split())
a_rev = a[::-1]
b_rev = b[::-1]
if int(a_rev) > int(b_rev):
    print(int(a_rev))
else:
    print(int(b_rev))