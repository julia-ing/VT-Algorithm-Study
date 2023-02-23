## 1. Longest Palindromic Substring

### 🔮 My solution

- 우선, 문자열이 들어왔을 때 팰린드롬인지 검사하는 함수를 만들어주었다.
- 참고로 팰린드롬은 대칭을 의미하므로, s와 s를 거꾸로 읽은 문자열이 같은 지 확인해주면 된다.
```python
def isPalindrome(self, s):
    return s == s[::-1]
```

- 그 후 솔루션 함수를 작성해주었는데, 처음에는 time exceeded 로 실패했다.

실패 코드:
```python
def longestPalindrome(self, s: str) -> str:
    max_palindrome = ""
    for i in range(len(s)+1):
        for j in range(i):
            target = s[j:i]
            if self.isPalindrome(target):
                if len(max_palindrome) < len(target):
                    max_palindrome = target
    return max_palindrome
```

- 아무래도 위 코드가 엄청난 brute force 여서 그런 것 같았다. 짧은 문자열부터 일일이 검사해주니까..
- 따라서 긴 부분 문자열부터 검사해주고, 팰린드롬을 찾는 즉시 리턴해주면 time limit 을 통과할 수 있을 것이다.

개선 코드:
```python
def longestPalindrome(self, s: str) -> str:
    for i in range(len(s)):
        for j in range(i+1):
            if self.isPalindrome(s[j:len(s) - i + j]):  # 긴 부분 문자열부터 체크; max 를 리턴하기 위함
                return s[j:len(s) - i + j]
```

### 🦦 Optimization (other solutions)

- 다른 솔루션으로는 투포인터 (window sliding) 가 있다.
- 홀수와 짝수를 나누어서 생각하는게 포인트인 것 같다. 
- expand 함수는 한 글자 혹은 두 글자를 중앙으로 해서, 팰린드롬이면 양 옆으로 포인터를 확장시킨다.

    ```python
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1] # 위에서 한번 더 빼/더해 주었으므로 되돌려놓음

        if len(s) == 1:  # 길이가 1이면 바로 리턴
            return s
            
        res = ""

        for i in range(len(s) - 1):
            # expand(i,i+1)는 홀수 팰린드롬, expand(i,i+2)는 짝수 팰린드롬 판단
            res = max(res, expand(i, i+1), expand(i, i+2), key=len)
        return res
    ```

### 👊 문제 회고
사실 투포인터나 dp로 풀고 싶었는데 둘 다 너무 생각하기 어려웠다 ㅜㅜ 

## 2. Top K Frequent Elements

### 🔮 My solution

- 단순하게 리스트 안의 숫자와 그 숫자가 나온 횟수를 dictionary에 저장해두고
-> 횟수 (value) 를 기준으로 정렬해서 key 를 k개만큼 리스트에 담아 리턴하는 풀이이다.

```python
def topKFrequent(self, nums, k):
    num_dict = {}
    res = []

    for n in nums:
        if n not in num_dict:
            num_dict[n] = 1
        else:
            num_dict[n] += 1
    num_dict = sorted(num_dict, key=num_dict.get, reverse=True)

    for i in range(k):
        res.append(num_dict[i])

    return res
```

- 완벽히 같은 풀이지만 좀 더 간결하게 쓸 수도 있다.
- `num_dict.get(i, 0)` 는 num_dict 에 i 가 있으면 get 해오고 없으면 0을 가져온다!!
요 아이를 쓰면 if else 로 번거롭게 나누지 않아도 돼서 편리할 것 같다.
```python
def topKFrequent(nums, k):
    num_dict = {}
    for i in nums:
        num_dict[i] = num_dict.get(i, 0) + 1
    return sorted(num_dict, key=num_dict.get, reverse=True)[0:k]
```

### 🦦 Optimization (other solutions)

- 문제 tag에 heap 이 있어서 heap 을 사용해보았다. 
- 시간 복잡도: O(NlogN)


- 나는 딕셔너리를 이용해서 횟수를 저장했는데, 파이썬은 대단했다.. 이런 기능이 다 함수로 내장되어있다..
**collections.Counter(nums)** 를 사용하면 바로 요소와 횟수를 딕셔너리에 저장해준다!!
- 이후 코드도 비슷하지만, heappush / heappop 을 사용한다.
- 참고로 힙은 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다. 그리고 파이썬 **heapq** 모듈은 우선 순위 큐 알고리즘을 제공한다. 
내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬된다.  
따라서 기본적으로 최소 힙 정렬이기 때문에 `heapq.heappop(heap)` 를 하면 heap에서 가장 작은 원소를 pop 해 온다.
- 우리는 최소 힙이 아니라 최대 힙 정렬이 필요하다. 따라서 이럴 때는 `heapq.heappush(heap, (-item))`
이런 식으로 음수 값을 push 해서 저장해주면 된다!! 그럼 자연스럽게 반대로 정렬되는 효과를 볼 수 있다. 

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = collections.Counter(nums)
    heap = []

    for key in count:
        heapq.heappush(heap, (-count[key], key))  # 순서를 위해 음수로 넣음
    
    res = []
    for _ in range(k):
        popped = heapq.heappop(heap)
        res.append(popped[1])
    
    return res
```

### 👊 문제 회고
가끔 문제 난이도가 잘못 나온 것 같을 때가 있다.. 미디움이 더 어려웠슴미다..
그래도 방심하지 말고 여러 풀이를 확인해보면서 배워야겠다!!
