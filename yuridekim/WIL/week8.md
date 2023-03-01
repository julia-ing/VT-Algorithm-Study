### **Week 8**
|                                  #                                   |            TITLE             |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:----------------------------------------:|
| [128](https://leetcode.com/problems/longest-consecutive-sequence/)    | Longest Consecutive Sequence     | Graph               | <span style="color:orange">Medium</span> |
| [128](https://leetcode.com/problems/find-median-from-data-stream/)               | Find Median from Data Stream               | Heap     | <span style="color:red">Hard</span>   |

### 200. Longest Consecutive Sequence
#### 문제풀이
```
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        sorted_nums = sorted(nums)
        a = sorted_nums[0]
        max_len = cur_len = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == a+1:
                cur_len += 1
            else:
                if cur_len > max_len: max_len = cur_len
                cur_len = 1
            a = sorted_nums[i]
            
        if cur_len > max_len: max_len = cur_len
        return max_len
```


#### 💡 What I learned!
계속 consecutive한 수열을 찾다가 다음 value가 이전 value+1가 아닐 때 count를 초기화하고 max와 비교하여 설정해준 다음 계속 탐색을 이어간다.


-------------------------------------------------------------------
### 295. Find Median from Data Stream
#### 문제풀이
Trial 1 Time Limit Exceeded
```
class MedianFinder(object):

    def __init__(self):
        self.num_list = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.num_list.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        sorted_list = sorted(self.num_list)
        n = len(self.num_list)
        if n % 2 == 0:
            return sorted_list[int(n/2) -1]/2.0 + sorted_list[int(n/2)]/2.0
        else:
            return sorted_list[int((n-1)/2)]
```

Trial 2 Time Limit Exceeded
```
class MedianFinder(object):

    def __init__(self):
        self.num_list = []
        self.count = 0
        self.low = None
        self.high = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.count += 1
        if self.count == 1:
            self.num_list.append(num)
            self.low = 0
            self.high = 0
        if self.num_list[-1] < num:
            self.num_list.append(num)
            if self.count % 2 ==0:
                self.high += 1
            else:
                self.low += 1
        elif num in self.num_list:
            idx = self.num_list.index(num)
            if self.count % 2 ==0:
                self.high += 1
            else:
                self.low += 1
        else:
            for i in range(len(self.num_list)):
                if self.num_list[i] > num:
                    self.num_list.insert(i, num)
                    break
            if self.count % 2 ==0:
                self.high += 1
            else:
                self.low += 1
        
    def findMedian(self):
        """
        :rtype: float
        """
        return (self.num_list[self.low] + self.num_list[self.high])/2.0

# For debugging        
med = MedianFinder()
med.addNum(6)
print(med.findMedian())
med.addNum(10)
print(med.findMedian())
med.addNum(2)
print(med.findMedian())
med.addNum(6)
print(med.findMedian())
med.addNum(5)
print(med.findMedian())
med.addNum(0)
print(med.findMedian())
med.addNum(6)
print(med.findMedian())
med.addNum(3)
print(med.findMedian())
med.addNum(1)
print(med.findMedian())
med.addNum(0)
print(med.findMedian())
med.addNum(0)
print(med.findMedian())
"""
med.addNum(1)
med.addNum(2)
print(med.findMedian())
med.addNum(3)
print(med.findMedian())


med.addNum(-1)
print(med.findMedian())
med.addNum(-2)
print(med.findMedian())
med.addNum(-3)
print(med.findMedian())
med.addNum(-4)
print(med.findMedian())
med.addNum(-5)
print(med.findMedian())

med.addNum(6)
print(med.findMedian())
med.addNum(10)
print(med.findMedian())
med.addNum(2)
print(med.findMedian())
med.addNum(6)
print(med.findMedian())
med.addNum(5)
print(med.findMedian())
```
두 번 다 timeout이 나서 실패했다. 너무 비싼 sorting을 사용했나보다.

#### 💡 What I learned!
```
from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []  # negative numbers for small
        self.large = []  # positive numbers for large

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
```
두번째 trial이랑 나름 비슷한(다고 생각했던) 로직으로 사람들 예시에서 heap을 사용을 했다. 미디언을 제일 앞에 값으로 갖도록 각각 large와 small 리스트를 따로 define해주는 방식이었다. 그래서 heapqpoppush을 이용했는데 먼저 지금 add 해주는 숫자를 heap에 넣어서 large에서는 가장 작은 숫자를 small로 옮겨준다. 또는 홀수일때는 small에서 large로 가장 큰 숫자를 옮겨줘야되는데 구현상 heapqpoppush는 가장 작은 숫자를 가져가니까 여기서 small은 오히려 negative하게 값들을 갖고 있어준다.