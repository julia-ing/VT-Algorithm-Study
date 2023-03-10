## 1. longest substring without repeating characters

### ๐ฎ My solution

- ๋ฌธ์ ๋ฅผ ๋ณด์๋ง์ dp์ ๊ฝํ์ dp ๋ฐฉ์์ผ๋ก ํ๋ค.
dp๋ก ํธ๋ ์์ค์ ์ ์ ํ๋ ค์ ํฌํฌ์ธํฐ๊ฐ ์๊ฐ๋ฌ์ง๋ง..

-์๊ฐ ๋ณต์ก๋: O(N^2)

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

### ๐ฆฆ Optimization (other solutions)

- ๋ค๋ฅธ ์๋ฃจ์์ผ๋ก๋ ํฌํฌ์ธํฐ (window sliding) ๊ฐ ์๋ค.

    ```python
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = res = 0
        for r in range(len(s)): # ๋ฌธ์์ด์ ๋ฌธ์ ๋ฐ๋ณต
            if s[r] not in seen: # dict์ ํ์ฌ ๋ฌธ์๊ฐ ์์ ๊ฒฝ์ฐ
                res = max(res, r-l+1) # window size๋ฅผ ๋๋ฆฐ๋ค
            else: # ๋ฐ๋ณต ๋ฌธ์๊ฐ ๋ํ๋ฌ์ ๊ฒฝ์ฐ
                if seen[s[r]] < l: # ๋ฌธ์๊ฐ ํ์ฌ ์๋์ฐ์ left pointer๋ณด๋ค ์ผ์ชฝ์ ์์ ๊ฒฝ์ฐ
                    res = max(res, r-l+1)
                else: # left pointer์ ์์น๋ฅผ ์๋ฐ์ดํธ ํด์ค๋ค.
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return res
    ```

### ๐ ๋ฌธ์  ํ๊ณ 
ํฌํฌ์ธํฐ ๋ฐฉ์์ ์์ง ์ต์ํ์ง ์์ ๊ฒ ๊ฐ๋ค.. ๊ณต๋ถํด์ผ์ง

## 2. Word Break

### ๐ฎ My solution

- ๋ฌธ์  Tag ๊ฐ dp์์ง๋ง Dp ๋ฐฉ์์ด ์ ๋ ์ค๋ฅด์ง ์์์ ์ฌ๊ท๋ก ๋จผ์  ์๋ํ๋ค.
- ์๊ฐ ๋ณต์ก๋: O(2^N)

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

### ๐ฆฆ Optimization (other solutions)

- ๋ค์์ ์๋ฃจ์์ ์ฐธ๊ณ ํ dp ์ฝ๋์ด๋ค. 
- ์๊ฐ ๋ณต์ก๋: O(N^3)

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

### ๐ ๋ฌธ์  ํ๊ณ 
dp ์์ฒด๊ฐ ์ฌ๊ท๋ฅผ ๊ฐ์ ํด๋ณด์๋ ์ฐจ์์์ ๋์ค๋ ๊ฑฐ๋๊น ํ๋ฆ ์์ฒด๋ ๋น์ทํ์ง๋ง,
dp ๋ฅผ ์ด๋ค ํํ์ array๋ก ์งํํ  ์ง ๊ฒฐ์ ํ๋ ๊ณผ์ ๊ณผ ๋ฆฌํดํด์ผ ํ๋ ๊ฐ์ด ๋ฌด์์ผ ์ง ๊ณ ๋ฏผํ๋ ๊ณผ์ ์์ ์ ๋ฅผ ๋จน์๋ค.
