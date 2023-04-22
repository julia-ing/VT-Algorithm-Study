import numpy as np

s = "xyb"
cur_s = np.array(list(s))
result = ""

while True:
    idx = np.argmax(cur_s)
    result = result + cur_s[idx]
    if idx == len(cur_s) - 1:
        break
    elif len(cur_s) == 1:
        result = result + s[idx + 1]
        break
    else:
        cur_s = np.array(list(cur_s[idx + 1 :]))

print(result)


# 더 좋은 풀이
s = "yxxyc"

string_stack = []

for i in s:
    while string_stack and string_stack[-1] < i: #지금들어온게 있던것보다 클때까지 pop
        string_stack.pop()
    string_stack.append(i)
print(''.join(string_stack))


