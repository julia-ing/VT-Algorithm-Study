### **Week 1**
|                                  #                                   |             TITLE              |        TAGS         |                DIFFICULTY                |
|:--------------------------------------------------------------------:|:------------------------------:|:-------------------:|:----------------------------------------:|
|             [1](https://leetcode.com/problems/two-sum/)              |            Two Sum             |        Array        |  <span style="color:green">Easy</span>   |
| [300](https://leetcode.com/problems/longest-increasing-subsequence/) | Longest Increasing Subsequence | Dynamic Programming | <span style="color:orange">Medium</span> |

##### #1 Two sum
Time complexity is O(n) with space complexity O(n). 

--------------------------------

##### #300 Longest Increasing Subsequence

DP should be the maximum value between current dp value or an incremented value of dp that comes before itself and is smaller than the current num array(idx is on the left=smaller and the value of each index smaller than the current).

Space is O(n).

Time complexity is O(n^2) but the suggest complexity is O(nlogn). Maybe use binary search?
