def quicksort(array, start, end):
  if start >= end: # 원소가 1개면 종료
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quicksort(array, start, right - 1)
  quicksort(array, right + 1, end)
quicksort(array, 0, len(array-1))
print(array)
