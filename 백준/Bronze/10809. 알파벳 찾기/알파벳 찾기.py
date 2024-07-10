S = input()
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = []
for i in letter:
    result.append(str(S.find(i)))
result_1 = " ".join(result)
print(result_1)