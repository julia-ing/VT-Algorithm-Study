n = 2
m = 15
a = [2,3]
# n = 3
# m = 4
# a = [3,5,7]
a.sort(reverse=True)
cnt = 0
flag = 0
for i in a:
    tmp = m//i
    cnt = cnt + tmp
    if m%i == 0:
        print(cnt)
        flag = 1
        break
    else:
        m = m - tmp * i
if flag == 0:
    print("-1")
