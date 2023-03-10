## 1. longest substring without repeating characters

### ๐ฎ My solution

- ์ค์์ํ, ์ฌ๊ท

```python
def kthSmallest(self, root, k):
    def inorder(root):
        if root:
            return inorder(root.left) + [root.val] + inorder(root.right)
        else:
            return []

    res = inorder(root)
    return res[k-1]
```

### ๐ฆฆ Optimization (other solutions)

---

### ๐ ๋ฌธ์  ํ๊ณ 
์ํํ๋ฉด์ ํ์์ ํ๋ ๋ฐฉ์์ ์์์ง๋ง + ๋ก ๋ฐ๋ก ๋ํด์ฃผ๋ ๊ฒ ์๊ฐ๋ณด๋ค ์ ๋ ์ค๋ฅด์ง ์์๋ ๊ฒ ๊ฐ๋ค.

## 2. House Robber

### ๐ฎ My solution

- Dp ๋ฐฉ์์ผ๋ก ์ ๊ทผํ๋ค.
- 3๊ฐ๊น์ง๋ ๋ฏธ๋ฆฌ dp array ๋ฅผ ์ฑ์๋๊ณ , ๊ทธ ๋ค์๋ถํฐ ๋น๊ตํ๋ฉด์ ์ฑ์์ค๋ค. ์ฐ์ํด์ ๋์ค๋ ๊ฐ์ ๋ํด์ฃผ์ง ๋ชปํ๋ฏ๋ก `max(dp[i - 2], dp[i - 3])` ์ ์์ ์ ๋ํด์ค๋ค. 
- ์๊ฐ ๋ณต์ก๋: O(N)

```python
def rob(self, nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]

    for i in range(3, n):
        dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])

    return max(dp[-1], dp[-2])

```

### ๐ฆฆ Optimization (other solutions)

- ๋ค์์ ์๋ฃจ์์ ์ฐธ๊ณ ํ ํฌํฌ์ธํฐ ํ์ด๋ฐฉ๋ฒ์ด๋ค.

```python
def rob(self, nums):
    last, now = 0, 0
    for i in nums:
        last, now = now, max(last + i, now)
    return now
```

### ๐ ๋ฌธ์  ํ๊ณ 
dp ๋ ์ด๋ ต์ง๋ง ์์๋ง ์ ์๊ฐํ๊ณ  ์ฐจ๊ทผ์ฐจ๊ทผ ๊ตฌํํ๋ฉด ๋ฐฐ์ ํ์ง ์๋๋น !

๋ค๋ฅธ ์๋ฃจ์์ ๊ฐ๋จํ์ง๋ง ๊ฐ์ธ์ ์ผ๋ก๋ ์ง๊ด์ ์ผ๋ก ์๊ฐ์ด ์ ์๋ผ์ ์ฐธ๊ณ ์ฉ์ผ๋ก๋ง ๋ณด๋ฉด ์ข์ ๊ฒ ๊ฐ๋ค.
