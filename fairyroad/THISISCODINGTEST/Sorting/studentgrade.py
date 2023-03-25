cnt = int(input())
dict = []

for x in range(cnt):
  input_data = input().split()
  dict.append((input_data[0], input_data[1]))

sorted_dict = sorted(array, key=lambda x: x[1])

for i in sorted_dict:
  print(i[0], end=' ')
