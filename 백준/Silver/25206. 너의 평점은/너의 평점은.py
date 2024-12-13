total_num = 0
total_score = 0

def to_score(s):
    score_list = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5,
                  "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
    return float(score_list[str(s)])

for _ in range(20):
    name, num, rate = map(str, input().split())
    if rate == "P":
        continue
    total_num += float(num)
    total_score += to_score(rate) * float(num)

print(total_score/total_num)