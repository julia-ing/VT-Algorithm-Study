## Heap 
class MedianFinder:
    def __init__(self):
        self.max_heap = [] # lower half to use the largest number 
        self.min_heap = [] # larger half to use the lowest number

    # Balance two heaps: max_heap contains one extra element
    def addNum(self, num: int) -> None:  # TC: O(logn)
        heappush(self.max_heap, -num) # muliply the number by -1 to use as max-heap
        popped_element = heappop(self.max_heap)
        heappush(self.min_heap, -popped_element)
        
        if len(self.max_heap) < len(self.min_heap):
            popped_element = heappop(self.min_heap)
            heappush(self.max_heap, -popped_element)
        
    # Even: (largest number in max heap + lowest number in min heap)/2
    # Odd: one extra element in max_heap
    def findMedian(self) -> float: # TC: O(1)
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]

'''
## List
class MedianFinder(object):
    def __init__(self):
        self.arr = []

    def addNum(self, num):
        self.arr.append(num)
        

    def findMedian(self):
        self.arr.sort() # TC: O(nlogn)

        mid = len(self.arr)//2
        if len(self.arr)%2 == 1:
            # middle value
            return float(self.arr[mid])
        else:
            # mean of the two middle values.
            return float(self.arr[mid-1]+self.arr[mid])/2
  '''
