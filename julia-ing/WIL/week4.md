## 1. longest substring without repeating characters

### 🔮 My solution

- 문제를 보자마자 dp에 꽂혀서 dp 방식으로 했다.
dp로 푸는 와중에 잘 안 풀려서 투포인터가 생각났지만..

-시간 복잡도: O(N^2)

```python
def lengthOfLongestSubstring(self, s):
    dp = [1] * len(s)
    char_idx_map = {}
    if s:
        char_idx_map[s[0]] = 0

    for i, char in enumerate(s[1:], start=1):
        if char not in char_idx_map:
            char_idx_map[char] = i
            dp[i] = dp[i - 1] + 1
        else:
            previous_idx = char_idx_map[char]
            dp[i] = min(i - previous_idx, dp[i - 1] + 1)
            char_idx_map[char] = i
    return max(dp) if dp else 0
```

### 🦦 Optimization (other solutions)

- 다른 솔루션으로는 투포인터 (window sliding) 가 있다.

    ```python
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = res = 0
        for r in range(len(s)): # 문자열의 문자 반복
            if s[r] not in seen: # dict에 현재 문자가 없을 경우
                res = max(res, r-l+1) # window size를 늘린다
            else: # 반복 문자가 나타났을 경우
                if seen[s[r]] < l: # 문자가 현재 윈도우의 left pointer보다 왼쪽에 있을 경우
                    res = max(res, r-l+1)
                else: # left pointer의 위치를 업데이트 해준다.
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return res
    ```

### 👊 문제 회고
투포인터 방식에 아직 익숙하지 않은 것 같다.. 공부해야징

## 2. Word Break

### 🔮 My solution

- 문제 Tag 가 dp였지만 Dp 방식이 잘 떠오르지 않아서 재귀로 먼저 시도했다.
- 시간 복잡도: O(2^N)

```python
def wordBreak(self, s, wordDict):
    def recurse(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and recurse(end):
                return True
        return False

    return recurse(0)
```

### 🦦 Optimization (other solutions)

- 다음은 솔루션을 참고한 dp 코드이다. 
- 시간 복잡도: O(N^3)

```python
def wordBreak(self, s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if s[j:i] in wordDict and dp[j]:
                dp[i] = True
                break
    return dp[len(s)]
```

### 👊 문제 회고
dp 자체가 재귀를 개선해보자는 차원에서 나오는 거니까 흐름 자체는 비슷했지만,
dp 를 어떤 형태의 array로 진행할 지 결정하는 과정과 리턴해야 하는 값이 무엇일 지 고민하는 과정에서 애를 먹었다.
