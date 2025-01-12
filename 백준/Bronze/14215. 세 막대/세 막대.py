def identify(box):
    if max(box) < sum(box) - max(box):
        return True
    else:
        return False

a, b, c = map(int, input().split())
box2 = [a,b,c]
while True:
    if identify(box2):
        print(sum(box2))
        break
    else:
        box2[box2.index(max(box2))] -= 1