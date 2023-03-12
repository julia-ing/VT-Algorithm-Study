# [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
**Algorithm**
- String, Two Pointer (Left / Right)

**Two Pointer Solution (runtime: 1038 ms)**
- Update the right pointer every iteration
- Update the left pointer when the right value is more lower than the left
```
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left] 
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
```

- Change `while` to `for-loop`
```
        for right in range(1, len(prices)):
            if prices[left] < prices[right]: # If there is a profit
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else: # If the right is more lower than the right
                left = right
```


**Explanation**
```
prices[left] --> buy stock (작은값일경우에만 계산, right 포인터에 더 작은값이 나오면 left 포인터 업데이트)
prices[right] --> sell stock (계속 업데이트)

Input: prices = [7,1,5,3,6,4]

step 1.
left = 0 -> right -> 1
right = 1 -> 2
max_profit = 0

step 2.
left = 1 
right = 2->3
max_profit =[2]-[1]=5-1=4

step 3.
left = 1 
right = 3 -> 4
max_profit =[3]-[1]=2 X

...
```

**Reference**
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/

**First Try (runtime: 929 ms)**
-  배열을 순서대로 순회하면서 최대값과 최솟값을 저장하고, 왼쪽에서부터 최솟값이 있을 경우 현재값과의 차이값을 구함 -> TLE
```
        min_price  = 10001
        max_profit = -1
        for price in prices:
            if min_price > price:
                min_price = price
            if min_price in prices:
                if price > min_price:
                    maxProfit = max(max_profit, price-min_price)

        return max(0, max_profit)
```
- 참고한 정답풀이
- `min_price`에 현재까지 살펴본 리스트의 최소값을 저장하고 , 그 다음 인덱스에서 최소값과 현재값의 차이인 `profit`을 계산하여 `max_profit`을 업데이트한다.
- 순서대로 보면서, 현재까지의 최소값과 그 다음 인덱스들을 순회하며 계산하기 때문에 잘 수행됨!
- `Two pointer`알고리즘 해법보다 빠름
```
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

```
