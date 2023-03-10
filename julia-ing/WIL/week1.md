## 1. two sum

### ๐ฎ My solution

- ์ฒซ๋ฒ์งธ๋ก ์๋ํ ์ฝ๋๋ brute force ๋ฐฉ์
- ์๊ฐ ๋ณต์ก๋: O(N^2)

```python
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### ๐ฆฆ Optimization (other solutions)

brute force ๋ฐฉ์์ ์ ๊ณฑ ์๊ฐ ๋ณต์ก๋๋ฅผ ๊ฐ์ง๊ธฐ ๋๋ฌธ์ ์ต์ ํ๋ ์ฝ๋๋ฅผ ์ํด ๊ตฌ๊ธ๋ง..

- ํ์ด์ฌ ๋ด์ฅ ํจ์ **in** ์ ์ฌ์ฉํ๋ฉด ์๊ฐ ๋ณต์ก๋๋ฅผ O(N) ์ผ๋ก ์ค์ผ ์ ์์!

    ```python
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            second = target - num
            if second in nums[i+1:]:
                return [i, nums[i+1:].index(second) + i + 1]
    ```
  enumerate() ์ ์ฌ์ฉํ๋ฉด ์ธ๋ฑ์ค์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ด ๋ฝ์ ์ ์๋ค. 
target ๋ฅผ ๋ง๋ค๊ธฐ ์ํด ํ์ํ ๊ฐ์ second ๋ณ์์ ์ ์ฅํ ํ, ๋ง์ฝ ๊ทธ ๊ฐ์ด ์์ง ๋์ง ์์ nums ๋ฆฌ์คํธ ๋ท๋ถ๋ถ์ ์กด์ฌํ๋ค๋ฉด
๊ทธ ๊ฐ์ ์ธ๋ฑ์ค๋ฅผ ์ฐพ์ i ์ ํจ๊ป ๋ฆฌํดํด์ค๋ค.


- **Hash Table (dictionary)**
    ```python
    def twoSum(self, nums, target):
        hashTable = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in hashTable:  # ๋๋จธ์ง ๊ฐ์ด ๋งต์ ์์ผ๋ฉด
                return sorted([i, hashTable[second]])  # ์ ์ฅ๋ ์ธ๋ฑ์ค๋ฅผ ๋ถ๋ฌ์ด
            hashTable[nums[i]] = i  # ์ซ์์ ์ธ๋ฑ์ค๋ฅผ ๋งต์ ์ ์ฅ
    ```
    ํด๋น ๋ฐฉ๋ฒ๋ ์๊ฐ ๋ณต์ก๋๋ O(N) ์ด๋ฉฐ maybe ์ด ๋ฌธ์ ์ ์ต์  ์ฝ๋์ผ ๋ฏ ํ๋ค. 
์ ๋ฐฉ์๊ณผ ๋์ผํ๊ฒ ๋๋จธ์ง ๊ฐ์ second ๋ณ์์ ์ ์ฅํด๋๊ณ  ๋์๋๋ฆฌ์ ์ ์ฅ๋์ด์๋์ง ํ์ธํ๋ค. 
๋ง์ฝ ์์ผ๋ฉด second ๋ฐ์ดํฐ์ ํด๋นํ๋ ์ธ๋ฑ์ค๋ฅผ i์ ํจ๊ป ๋ฆฌํดํด์ค๋ค. ์ฐธ๊ณ ๋ก sorted๋ ์์ด๋ ๋ฌธ์  ํต๊ณผํ๊ธฐ๋ ํ๋ค..
๊ทธ๋ฆฌ๊ณ  ์์์ ๋ฆฌํด๋์ง ์๋๋ค๋ฉด ํด์ํ์ด๋ธ ์ฆ ๋์๋๋ฆฌ์ ๊ฐ์ ์ ์ฅํ๋ค. (key๋ nums[i] ์ฆ ๋ฐ์ดํฐ, value๋ ์ธ๋ฑ์ค)

### ๐ ๋ฌธ์  ํ๊ณ 

๊ฐ์ธ์ ์ผ๋ก ์ฒ์๋ถํฐ ์ต์ ์ ์ฝ๋๋ฅผ ์ง๋๊ฑด ์์ง ์ด๋ ต๋ค. ์ด ๋ฌธ์ ๋ ๊ตฌ๊ธ๋ง ์ ๊น์ง๋ ์ฝ๊ฒ ๋ ์ค๋ฅด๋ ํ์ด๊ฐ brute force ๋ฐ์ ์์๊ธฐ ๋๋ฌธ์.. ์์ง ๊ฐ ๊ธธ์ด ๋จผ ๊ฒ ๊ฐ๋ค ^0^
ํด๋น ๋ฌธ์ ์์ ์ธ์๊น์๋ ๊ฒ์ ํด์ํ์ด๋ธ์ ์ด์ฉํ 3๋ฒ ํ์ด์๋๋ฐ,
๋์๋๋ฆฌ๋ฅผ ์ ํ์ฉํ๋ฉด ์ํ๋ ๊ฐ์ ๋ฐ๋ก ์ฐพ์์ฌ ์ ์๊ณ  ์๊ฐ๋ณต์ก๋๋ ์ค์ผ ์ ์๋ค๋ ์ฌ์ค์ ์์ง ๋ง์!

## 2. longest increasing subsequence

### ๐ฎ My solution

- ์ฒซ๋ฒ์งธ๋ก ์๋ํ ์ฝ๋๋ commonํ dynamic programming ๋ฐฉ์
- ์๊ฐ ๋ณต์ก๋: O(N^2)
  - ์์:
    - nums = [10,9,2,5,3,7,101,18]
    - dp 
      - i = 0: [1,1,1,1,1,1,1,1]
      - i = 1: [1,1,1,1,1,1,1,1]
      - i = 2: [1,1,1,1,1,1,1,1]
      - i = 3: [1,1,1,2,1,1,1,1]
      - i = 4: [1,1,1,2,2,1,1,1]
      - i = 5: [1,1,1,2,2,3,1,1]
      - i = 6: [1,1,1,2,2,3,4,1]
      - i = 7: [1,1,1,2,2,3,4,4]
      - result : max 4

```python
def lengthOfLIS(self, nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### ๐ฆฆ Optimization (other solutions)

- **binary search**

์ด์งํ์์ ์ด์ฉํ๋ฉด ์๊ฐ๋ณต์ก๋๋ฅผ O(NlogN) ์ผ๋ก ๋ง๋ค ์ ์์!
**bisect_left** ? - ์ฐธ๊ณ : [bisect_left, biseft_right](https://folivora.tistory.com/83)

์์: nums = [10,9,2,5,3,7,101,18]
1. tmp = [10]
2. for loop
   1. x = 9, tmp = [9]
   2. x = 2, tmp = [2]
   3. x = 5, tmp = [2,5]
   4. x = 3, idx = 1, tmp = [2,3]
   5. x = 7, tmp = [2,3,7]
   6. x = 101, tmp = [2,3,7,101]
   7. x = 18, idx = 3, tmp = [2,3,7,18]
3. return length 4

```python
def lengthOfLIS(self, nums):
    tmp = [nums[0]]
    for x in nums[1:]:
        if tmp[-1] < x:  # x๊ฐ ๋ฆฌ์คํธ ๋ง์ง๋ง ์์๋ณด๋ค ํฌ๋ฉด
            tmp.append(x)
        else:
            idx = bisect_left(tmp, x)  # x๋ฅผ ์ฝ์ํ  ์์น๋ฅผ ์ฐพ์ ํด๋น ์์น์ ๊ฐ์ ๊ฐ์ ๋ผ์ด๋ค
            tmp[idx] = x
    return len(tmp)
```

### ๐ ๋ฌธ์  ํ๊ณ 
๋ฌธ์ ๋ฅผ ๋ณด๊ณ  DP ๋ฅผ ์ฌ์ฉํด์ผ๊ฒ ๋ค๊ณ  ์๊ฐํด ๋ค์ด๋๋ฏน์ผ๋ก ํ์์ง๋ง, ์ญ์ ๋ณด๋ค ์ข์ ํ์ด๊ฐ ์์๋ค.
๋ฆฌ์คํธ๋ฅผ bisect_left๋ฅผ ์ฌ์ฉํด ๊ฐ์๋ผ์ฐ๋ ๋ฐฉ์์ผ๋ก ์ต์ ํํ๋ ๋ฐฉ๋ฒ์ด์๋๋ฐ,
์์ผ๋ก ๋ฆฌ์คํธ ๊ด๋ จ ์ต์ ํ๋ฅผ ๊ณ ๋ฏผํ  ๋ binary๋ฅผ ํ๋์ ์๋จ์ผ๋ก ์ ๋ ์ฌ๋ ธ์ผ๋ฉด ์ข๊ฒ ๋ค!
