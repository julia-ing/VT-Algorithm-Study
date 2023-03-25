a = [1,2,5,4,3]
b = [5,5,6,6,5]
k = 3
a.sort()
b.sort(reverse=True)
print(sum(a[k:] + b[:k]))
