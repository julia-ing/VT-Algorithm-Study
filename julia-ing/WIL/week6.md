## 1. Longest Palindromic Substring

### ๐ฎ My solution

- ์ฐ์ , ๋ฌธ์์ด์ด ๋ค์ด์์ ๋ ํฐ๋ฆฐ๋๋กฌ์ธ์ง ๊ฒ์ฌํ๋ ํจ์๋ฅผ ๋ง๋ค์ด์ฃผ์๋ค.
- ์ฐธ๊ณ ๋ก ํฐ๋ฆฐ๋๋กฌ์ ๋์นญ์ ์๋ฏธํ๋ฏ๋ก, s์ s๋ฅผ ๊ฑฐ๊พธ๋ก ์ฝ์ ๋ฌธ์์ด์ด ๊ฐ์ ์ง ํ์ธํด์ฃผ๋ฉด ๋๋ค.
```python
def isPalindrome(self, s):
    return s == s[::-1]
```

- ๊ทธ ํ ์๋ฃจ์ ํจ์๋ฅผ ์์ฑํด์ฃผ์๋๋ฐ, ์ฒ์์๋ time exceeded ๋ก ์คํจํ๋ค.

์คํจ ์ฝ๋:
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

- ์๋ฌด๋๋ ์ ์ฝ๋๊ฐ ์์ฒญ๋ brute force ์ฌ์ ๊ทธ๋ฐ ๊ฒ ๊ฐ์๋ค. ์งง์ ๋ฌธ์์ด๋ถํฐ ์ผ์ผ์ด ๊ฒ์ฌํด์ฃผ๋๊น..
- ๋ฐ๋ผ์ ๊ธด ๋ถ๋ถ ๋ฌธ์์ด๋ถํฐ ๊ฒ์ฌํด์ฃผ๊ณ , ํฐ๋ฆฐ๋๋กฌ์ ์ฐพ๋ ์ฆ์ ๋ฆฌํดํด์ฃผ๋ฉด time limit ์ ํต๊ณผํ  ์ ์์ ๊ฒ์ด๋ค.

๊ฐ์  ์ฝ๋:
```python
def longestPalindrome(self, s: str) -> str:
    for i in range(len(s)):
        for j in range(i+1):
            if self.isPalindrome(s[j:len(s) - i + j]):  # ๊ธด ๋ถ๋ถ ๋ฌธ์์ด๋ถํฐ ์ฒดํฌ; max ๋ฅผ ๋ฆฌํดํ๊ธฐ ์ํจ
                return s[j:len(s) - i + j]
```

### ๐ฆฆ Optimization (other solutions)

- ๋ค๋ฅธ ์๋ฃจ์์ผ๋ก๋ ํฌํฌ์ธํฐ (window sliding) ๊ฐ ์๋ค.
- ํ์์ ์ง์๋ฅผ ๋๋์ด์ ์๊ฐํ๋๊ฒ ํฌ์ธํธ์ธ ๊ฒ ๊ฐ๋ค. 
- expand ํจ์๋ ํ ๊ธ์ ํน์ ๋ ๊ธ์๋ฅผ ์ค์์ผ๋ก ํด์, ํฐ๋ฆฐ๋๋กฌ์ด๋ฉด ์ ์์ผ๋ก ํฌ์ธํฐ๋ฅผ ํ์ฅ์ํจ๋ค.

    ```python
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1] # ์์์ ํ๋ฒ ๋ ๋นผ/๋ํด ์ฃผ์์ผ๋ฏ๋ก ๋๋๋ ค๋์

        if len(s) == 1:  # ๊ธธ์ด๊ฐ 1์ด๋ฉด ๋ฐ๋ก ๋ฆฌํด
            return s
            
        res = ""

        for i in range(len(s) - 1):
            # expand(i,i+1)๋ ํ์ ํฐ๋ฆฐ๋๋กฌ, expand(i,i+2)๋ ์ง์ ํฐ๋ฆฐ๋๋กฌ ํ๋จ
            res = max(res, expand(i, i+1), expand(i, i+2), key=len)
        return res
    ```

### ๐ ๋ฌธ์  ํ๊ณ 
์ฌ์ค ํฌํฌ์ธํฐ๋ dp๋ก ํ๊ณ  ์ถ์๋๋ฐ ๋ ๋ค ๋๋ฌด ์๊ฐํ๊ธฐ ์ด๋ ค์ ๋ค ใใ 

## 2. Top K Frequent Elements

### ๐ฎ My solution

- ๋จ์ํ๊ฒ ๋ฆฌ์คํธ ์์ ์ซ์์ ๊ทธ ์ซ์๊ฐ ๋์จ ํ์๋ฅผ dictionary์ ์ ์ฅํด๋๊ณ 
-> ํ์ (value) ๋ฅผ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌํด์ key ๋ฅผ k๊ฐ๋งํผ ๋ฆฌ์คํธ์ ๋ด์ ๋ฆฌํดํ๋ ํ์ด์ด๋ค.

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

- ์๋ฒฝํ ๊ฐ์ ํ์ด์ง๋ง ์ข ๋ ๊ฐ๊ฒฐํ๊ฒ ์ธ ์๋ ์๋ค.
- `num_dict.get(i, 0)` ๋ num_dict ์ i ๊ฐ ์์ผ๋ฉด get ํด์ค๊ณ  ์์ผ๋ฉด 0์ ๊ฐ์ ธ์จ๋ค!!
์ ์์ด๋ฅผ ์ฐ๋ฉด if else ๋ก ๋ฒ๊ฑฐ๋กญ๊ฒ ๋๋์ง ์์๋ ๋ผ์ ํธ๋ฆฌํ  ๊ฒ ๊ฐ๋ค.
```python
def topKFrequent(nums, k):
    num_dict = {}
    for i in nums:
        num_dict[i] = num_dict.get(i, 0) + 1
    return sorted(num_dict, key=num_dict.get, reverse=True)[0:k]
```

### ๐ฆฆ Optimization (other solutions)

- ๋ฌธ์  tag์ heap ์ด ์์ด์ heap ์ ์ฌ์ฉํด๋ณด์๋ค. 
- ์๊ฐ ๋ณต์ก๋: O(NlogN)


- ๋๋ ๋์๋๋ฆฌ๋ฅผ ์ด์ฉํด์ ํ์๋ฅผ ์ ์ฅํ๋๋ฐ, ํ์ด์ฌ์ ๋๋จํ๋ค.. ์ด๋ฐ ๊ธฐ๋ฅ์ด ๋ค ํจ์๋ก ๋ด์ฅ๋์ด์๋ค..
**collections.Counter(nums)** ๋ฅผ ์ฌ์ฉํ๋ฉด ๋ฐ๋ก ์์์ ํ์๋ฅผ ๋์๋๋ฆฌ์ ์ ์ฅํด์ค๋ค!!
- ์ดํ ์ฝ๋๋ ๋น์ทํ์ง๋ง, heappush / heappop ์ ์ฌ์ฉํ๋ค.
- ์ฐธ๊ณ ๋ก ํ์ ์์  ์ด์ง ํธ๋ฆฌ์ ์ผ์ข์ผ๋ก ์ฐ์ ์์ ํ๋ฅผ ์ํ์ฌ ๋ง๋ค์ด์ง ์๋ฃ๊ตฌ์กฐ์ด๋ค. ๊ทธ๋ฆฌ๊ณ  ํ์ด์ฌ **heapq** ๋ชจ๋์ ์ฐ์  ์์ ํ ์๊ณ ๋ฆฌ์ฆ์ ์ ๊ณตํ๋ค. 
๋ด๋ถ์ ์ผ๋ก๋ ์ธ๋ฑ์ค 0์์ ์์ํด k๋ฒ์งธ ์์๊ฐ ํญ์ ์์ ์์๋ค(2k+1, 2k+2) ๋ณด๋ค ์๊ฑฐ๋ ๊ฐ์ ์ต์ ํ์ ํํ๋ก ์ ๋ ฌ๋๋ค.  
๋ฐ๋ผ์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ต์ ํ ์ ๋ ฌ์ด๊ธฐ ๋๋ฌธ์ `heapq.heappop(heap)` ๋ฅผ ํ๋ฉด heap์์ ๊ฐ์ฅ ์์ ์์๋ฅผ pop ํด ์จ๋ค.
- ์ฐ๋ฆฌ๋ ์ต์ ํ์ด ์๋๋ผ ์ต๋ ํ ์ ๋ ฌ์ด ํ์ํ๋ค. ๋ฐ๋ผ์ ์ด๋ด ๋๋ `heapq.heappush(heap, (-item))`
์ด๋ฐ ์์ผ๋ก ์์ ๊ฐ์ push ํด์ ์ ์ฅํด์ฃผ๋ฉด ๋๋ค!! ๊ทธ๋ผ ์์ฐ์ค๋ฝ๊ฒ ๋ฐ๋๋ก ์ ๋ ฌ๋๋ ํจ๊ณผ๋ฅผ ๋ณผ ์ ์๋ค. 

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = collections.Counter(nums)
    heap = []

    for key in count:
        heapq.heappush(heap, (-count[key], key))  # ์์๋ฅผ ์ํด ์์๋ก ๋ฃ์
    
    res = []
    for _ in range(k):
        popped = heapq.heappop(heap)
        res.append(popped[1])
    
    return res
```

### ๐ ๋ฌธ์  ํ๊ณ 
๊ฐ๋ ๋ฌธ์  ๋์ด๋๊ฐ ์๋ชป ๋์จ ๊ฒ ๊ฐ์ ๋๊ฐ ์๋ค.. ๋ฏธ๋์์ด ๋ ์ด๋ ค์ ์ด๋ฏธ๋ค..
๊ทธ๋๋ ๋ฐฉ์ฌํ์ง ๋ง๊ณ  ์ฌ๋ฌ ํ์ด๋ฅผ ํ์ธํด๋ณด๋ฉด์ ๋ฐฐ์์ผ๊ฒ ๋ค!!
