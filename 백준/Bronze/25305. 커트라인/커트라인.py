N, k = map(int, input().split())
score = input().split(" ")
int_score = [int(x) for x in score]
int_score.sort(reverse=True)
print(int_score[k-1])