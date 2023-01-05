## Two Sum

### Understanding problem

Find the entire problem here: https://leetcode.com/problems/two-sum/

As per the problem we have been given an array of integers & a target
```java
Integer[] numbers = {1,2,3,4};
int target = 5
```
Our goal is to find the indices of two integers that adds to the target.

### First Thought About Solution (Brute force)

We can run two for loop and check the addition result for each combination & if it matches with the target then keep the indices of two numbers and return it. Time complexity would be O(N²) and Space complexity O(1).

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }

        return null;
    }
}
```

### Second Thought About Solution (Hash map)

But can we do better? Each target is the addition result of two numbers: x+y=target; so we can find x=target-y then our job is done.
We have map data structure that can look up a key/value without looping n elements. That's the advantage we get for TC, but we add SC of O(N).
```java
class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            Integer idx = map.get(diff);

            if (map.containsKey(target - nums[i])) {
                return new int[] {idx, i};
            }

            map.put(nums[i], i);
        }

        return null;
    }
}
```

## Longest Increasing Subsequence

### First Thought About Solution (Dynamic Programming)

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int len = nums.length;
        int[] dp = new int[len];
        dp[0] = 1;
        int ans = 1;

        for (int i = 1; i < len; i++) {

            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                else {
                    dp[i] = Math.max(dp[i], 1);
                }
            }

            ans = Math.max(ans, dp[i]);
        }

        return ans;
    }
}
```

<img src = "https://user-images.githubusercontent.com/82510378/210799796-cf2f6cef-4f5c-4a01-ad19-abeb774025be.png" width="250px" height="250px">

### Second Thought About Solution (Binary Search)
```java
 public class Solution2 {
     public int lengthOfLIS(int[] nums) {
         int len = nums.length;
         int[] dp = new int[len];
         int ans = 0;

         for (int num : nums) {
             int idx = Arrays.binarySearch(dp, 0, ans, num);
             if (idx < 0) {
                 idx = -(idx + 1);
             }
             dp[idx] = num;
             if (idx == ans) {
                 ans++;
             }
         }

         return ans;
     }
 }
 ```
 
 <img src = "https://user-images.githubusercontent.com/82510378/210800495-813a0faf-df47-4dba-85a7-b5df4dbf1b1b.png" width="250px" height="250px">

#### Always welcome any feedbacks & Comments! 😊

