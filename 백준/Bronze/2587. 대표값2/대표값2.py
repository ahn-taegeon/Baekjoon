box = []
for _ in range(5):
    n = int(input())
    box.append(n)
box = sorted(box)
print(int(sum(box)/5))
print(box[2])