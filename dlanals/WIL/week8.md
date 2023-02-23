# 128. Longest Consecutive Sequence
- Medium

## 의식의 흐름
- 리스트 정렬
- 처음부터 순회하면서 max_length 갱신
- ex) nums = [100, 4, 200, 1, 3, 2]일때
  - 정렬하면 [1, 2, 3, 4, 100, 200]
  - n번째원소 = n-1번째원소 + 1이면 cnt += 1
  - consecutive가 아니면 cnt > max_length인지 확인 -> 맞으면 max_length갱신, cnt 다시 0으로 초기화
  - 초반 코드
  - ```python
    class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        cnt = 1
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                if cnt > max_length : max_length = cnt
                cnt = 1

        return max_length
    ```
    같은 원소를 가진 경우 오답 발생
    
    ![image](https://user-images.githubusercontent.com/97150219/220970232-36a1cdbd-8de6-43dc-afb8-12ee3fd0dea3.png)
   - trace해보기
   - ![image](https://user-images.githubusercontent.com/97150219/220970973-161d708d-2dda-4929-83da-49fc3b88cf69.png)
   - 원소 전체가 연속적인 경우 max_length를 갱신할 기회가 없었음
   - 따라서 return값을 max(cnt, max_length)로 바꿔주었음
   - submit했더니 또 에러발생 -> 원소가 0개일때
   - 또다른 오답
   - ![image](https://user-images.githubusercontent.com/97150219/220972434-2c46a732-d2f4-41e6-b67c-ed37ca1323a1.png)
   - 같은 원소가 존재할때도 생각해줘야함 -> 이부분은 list 대신 set 사용해도 (중복 제거)
   - 까지 완료했더니 accept되었다

## 관련 개념
### HashSet
- 찾아보니 java에서 주로 사용하는 데이터구조인듯하다.
- python set 개념과 hash 개념을 결합해서 새로 만들어낸듯하다.

## Solution
### Sorting
- Time Complexity : O(nlgn)
  - The main for loop does constant work nnn times,
  - so the algorithm's time complexity is dominated by the invocation of sort,
  - which will run in O(nlgn) time for any sensible implementation.
- Space Complexity : O(1) or O(n)
  - For the implementations provided here, the space complexity is constant because we sort the input array in place.
  - If we are not allowed to modify the input array, we must spend linear space to store a sorted copy.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        cnt = 1
        max_length = 1

        if len(nums) == 0: return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if cnt > max_length : max_length = cnt
                cnt = 1
            
        return max(cnt, max_length)
```

### HashSet and Intelligent Sequence Building
- 이런 솔루션도 있구나~하고 새로 알게된 솔루션
- Time Complexity : O(n)
  - Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear.
  - Because the while loop is reached only when currentNum marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), the while loop can only run for nnn iterations throughout the entire runtime of the algorithm.
  - This means that despite looking like O(n⋅n) complexity, the nested loops actually run in O(n+n)=O(n) time.
  - All other computations occur in constant time, so the overall runtime is linear.
- Space Complexity : O(n)
  - In order to set up O(1) containment lookups, we allocate linear space for a hash table to store the O(n) numbers in nums.
  - Other than that, the space complexity is identical to that of the brute force solution.
- brute force 방법의 시간복잡도 문제를 해결하기 위한 솔루션
- the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups
- only attempt to build sequences from numbers that are not already part of a longer sequence.
- This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.

```python
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums) # nums -> set

        for num in num_set:
            if num - 1 not in num_set: # consecutive하지 않을 때
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set: # 
                    current_num += 1 # 
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```


# 295. Find Median from Data Stream
- Hard

## 의식의 흐름
- 개념 자체는 쉬운듯 하지만 클래스 구현 문제는 오랜만이라 문법이 갑자기 헷갈렸다.
- input값으로 두개의 리스트가 주어지는건가? addNum(num)이라는걸 보니 아닌것같다.
- Follow up의 optimization은 어떻게 구현할 수 있을까?

## Solution

```python
class MedianFinder:

    def __init__(self):
      self.arr = [] 

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        l = len(self.arr)
        
        if l%2 == 1:
            return self.arr[l//2]
        else:
            return (self.arr[l//2-1] + self.arr[l//2])/2

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```


# 느낀점
- 시간 더 투자하기 챌린지 중인데, 문제풀이 뿐만 아니라 집중 지속기간도 늘어나는 것이 벌써 느껴진다.
- 실력이 늘 때까지 이렇게 시간을 넉넉하게 두다가, 어느 정도 숙달되면 문제 풀이 시간을 줄이는 훈련도 시작해야겠다.
