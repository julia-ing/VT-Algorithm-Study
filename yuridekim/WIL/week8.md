### **Week 8**
|                                  #                                   |            TITLE             |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:----------------------------------------:|
| [128](https://leetcode.com/problems/longest-consecutive-sequence/)    | Longest Consecutive Sequence     | Graph               | <span style="color:orange">Medium</span> |
| [128](https://leetcode.com/problems/find-median-from-data-stream/)               | Find Median from Data Stream               | Heap     | <span style="color:red">Hard</span>   |

### 200. Longest Consecutive Sequence
#### ๋ฌธ์ ํ์ด
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


#### ๐ก What I learned!
๊ณ์ consecutiveํ ์์ด์ ์ฐพ๋ค๊ฐ ๋ค์ value๊ฐ ์ด์  value+1๊ฐ ์๋ ๋ count๋ฅผ ์ด๊ธฐํํ๊ณ  max์ ๋น๊ตํ์ฌ ์ค์ ํด์ค ๋ค์ ๊ณ์ ํ์์ ์ด์ด๊ฐ๋ค.


-------------------------------------------------------------------
### 295. Find Median from Data Stream
#### ๋ฌธ์ ํ์ด
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
๋ ๋ฒ ๋ค timeout์ด ๋์ ์คํจํ๋ค. ๋๋ฌด ๋น์ผ sorting์ ์ฌ์ฉํ๋๋ณด๋ค.

#### ๐ก What I learned!
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
๋๋ฒ์งธ trial์ด๋ ๋๋ฆ ๋น์ทํ(๋ค๊ณ  ์๊ฐํ๋) ๋ก์ง์ผ๋ก ์ฌ๋๋ค ์์์์ heap์ ์ฌ์ฉ์ ํ๋ค. ๋ฏธ๋์ธ์ ์ ์ผ ์์ ๊ฐ์ผ๋ก ๊ฐ๋๋ก ๊ฐ๊ฐ large์ small ๋ฆฌ์คํธ๋ฅผ ๋ฐ๋ก defineํด์ฃผ๋ ๋ฐฉ์์ด์๋ค. ๊ทธ๋์ heapqpoppush์ ์ด์ฉํ๋๋ฐ ๋จผ์  ์ง๊ธ add ํด์ฃผ๋ ์ซ์๋ฅผ heap์ ๋ฃ์ด์ large์์๋ ๊ฐ์ฅ ์์ ์ซ์๋ฅผ small๋ก ์ฎ๊ฒจ์ค๋ค. ๋๋ ํ์์ผ๋๋ small์์ large๋ก ๊ฐ์ฅ ํฐ ์ซ์๋ฅผ ์ฎ๊ฒจ์ค์ผ๋๋๋ฐ ๊ตฌํ์ heapqpoppush๋ ๊ฐ์ฅ ์์ ์ซ์๋ฅผ ๊ฐ์ ธ๊ฐ๋๊น ์ฌ๊ธฐ์ small์ ์คํ๋ ค negativeํ๊ฒ ๊ฐ๋ค์ ๊ฐ๊ณ  ์์ด์ค๋ค.