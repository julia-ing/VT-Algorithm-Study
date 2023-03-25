def quicksort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  
  left_side = [for x in tail if x<=pivot]
  right_side = [for x in tail if x>pivot]
  return quicksort(left_side) + [pivot] + quicksort(right_side)

print(quicksort(array))
