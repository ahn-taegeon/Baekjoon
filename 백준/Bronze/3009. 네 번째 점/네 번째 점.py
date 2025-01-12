x = []
y = []
for _ in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
for X in x:
    num = x.count(X)
    if num == 1:
        x_r = X
for Y in y:
    num = y.count(Y)
    if num == 1:
        y_r = Y
print(x_r,y_r)