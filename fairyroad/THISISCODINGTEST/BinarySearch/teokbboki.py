M = 6
a = [19, 15, 10, 17]
a.sort(reverse=True)
for idx in range(max(a) - 1, 0, -1):
    result = 0
    for elem in a:
        tmp = elem - idx
        if tmp > 0:
            result += tmp
        else:
            break
    if result >= M:
        print(idx)
        break
