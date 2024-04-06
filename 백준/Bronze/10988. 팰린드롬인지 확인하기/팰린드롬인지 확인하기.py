s = input()
list_s = []
for i in range(len(s)):
    list_s.append(s[i])
a = list(reversed(list_s))
if list_s == a:
    print('1')
else:
    print('0')