n=[]
for i in range(10):
    b=int(input())
    n.append(b%42)
print(len(set(n)))