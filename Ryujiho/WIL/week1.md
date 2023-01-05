# Problem 1 (Two Sum)
- Array
- https://leetcode.com/problems/two-sum/
- 처음에는 Array를 순회하며 비교하는 O(n^2) 방식을 생각했다.
- leetcode 다른 풀이를 참고해보니 hash table를 적용하여 두 값의 차이를 index로 구현한 방법이 훨씬 간단하고 최적화된 것 같아 다시 작성했다.

# Problem 300 (Longest Increasing Subsequence)
- Dynamic Programming, 
- https://leetcode.com/problems/longest-increasing-subsequence/
- 단순하게 모든 원소들을 비교하고 최대길이의 subseqence 를 누적하여 max()로 출력하는 방식으로 구했는데 최적화 방법을 좀 더 생각해봐야겠다.
