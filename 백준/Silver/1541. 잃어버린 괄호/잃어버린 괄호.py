formula = str(input())
formula = formula.replace('+',' +')
formula = formula.replace('-',' -')
box = formula.split()

minus = []
num_zero_1 = box.count('0')
num_zero_2 = box.count('+0')
num_zero_3 = box.count('-0')
if num_zero_1 == 0:
    pass
else:
    for _ in range(num_zero_1):
        box.remove('0')
if num_zero_2 == 0:
    pass
else:
    for _ in range(num_zero_2):
        box.remove('+0')
if num_zero_3 == 0:
    pass
else:
    for _ in range(num_zero_3):
        box.remove('-0')
summation = 0
for i in range(len(box)):
    if int(box[i]) < 0 :
        minus.append(i)
if len(minus) == 0:
    for m in range(len(box)):
        summation += int(box[m])
else:
    start = min(minus)
    for m in range(start):
        summation += int(box[m])
    for s in range(start, len(box)):
        if int(box[s]) < 0:
            summation += int(box[s])
        else:
            summation -= int(box[s])
print(summation)