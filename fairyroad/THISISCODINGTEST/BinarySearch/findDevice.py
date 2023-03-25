n = 5
a = [8,3,7,9,2]
m = 3
b = [5,7,9]

a.sort()
for idx in b:
    if idx in a:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
print('\n')
