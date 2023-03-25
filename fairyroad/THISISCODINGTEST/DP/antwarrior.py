a = [1,3,2,4,6,7]

if len(a) <= 2:
    print(max(a))
elif len(a) == 3:
    print(max(max(a), a[0] + a[2]))
else:
    for i in range(3, len(a)):
        a[i] += max(a[i-2], a[i-3])
print(max(a))
