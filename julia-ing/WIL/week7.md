## 1. longest substring without repeating characters

### 🔮 My solution

- 중위순회, 재귀

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

### 🦦 Optimization (other solutions)

---

### 👊 문제 회고
순회하면서 탐색을 하는 방식은 알았지만 + 로 바로 더해주는 게 생각보다 잘 떠오르지 않았던 것 같다.

## 2. House Robber

### 🔮 My solution

- Dp 방식으로 접근했다.
- 3개까지는 미리 dp array 를 채워놓고, 그 다음부터 비교하면서 채워준다. 연속해서 나오는 값은 더해주지 못하므로 `max(dp[i - 2], dp[i - 3])` 에 자신을 더해준다. 
- 시간 복잡도: O(N)

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

### 🦦 Optimization (other solutions)

- 다음은 솔루션을 참고한 투포인터 풀이방법이다.

```python
def rob(self, nums):
    last, now = 0, 0
    for i in nums:
        last, now = now, max(last + i, now)
    return now
```

### 👊 문제 회고
dp 는 어렵지만 수식만 잘 생각하고 차근차근 구현하면 배신하지 않는당 !

다른 솔루션은 간단하지만 개인적으로는 직관적으로 생각이 잘 안돼서 참고용으로만 보면 좋을 것 같다.
