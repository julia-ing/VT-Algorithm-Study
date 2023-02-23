# 230. Kth Smallest Element in a BST
- Medium

## 의식의 흐름
- 트리 전부 순회하면서 먼저 정렬
- Follow up 부분) 연산으로 인해 트리가 변형될때마다 k번째 작은 값을 찾으려면 매번 정렬을 하기엔 복잡도가 너무 올라가지 않을까?

## 관련 개념
### Search
- 컴퓨터가 가장 많이 수행하는 연산 중 하나 -> 탐색의 시간효율성 증가시킬 수 있는 자료구조 및 알고리즘 필수
- 다수의 항목 중 원하는 항목을 찾는 연산
- 기본적인 Search Algorithm
  - Linear Search
    - 정렬되지 않은 python list 또는 linked list에서 사용하는 알고리즘
    - 처음 항목부터 마지막 항목까지 하나씩 검사하면서 특정 값(Search Key)과 동일한 키 값을 가지는 항목을 찾는 방법
    - 시간복잡도 : O(n)
  - Binary Search
    - 정렬된 python list(혹은 정적, 동적 배열)를 중간에 위치한 항목을 기준으로 두 부분으로 나누어가며 Search Key와 동일한 값을 가지는 항목을 찾는 방법
    - 시간복잡도 : O(n)
    - N개의 item으로 구성돼있는 정렬된 python list L이라고 가정
    - 1번의 비교 후에 L의 1/2, 즉 앞부분이나 뒷부분을 검색 키와 동일한 키 값을 가지는 항목을 찾을 때까지 (최악의 경우 하나의 항목만 남을때까지) 재귀호출
    - N개의 item들이 1개가 될 때까지 최대 몇번의 재귀 호출을 해야 하는지, 즉 N/2^k = 1에서 k의 값을 결정하면 항목 비교 횟수를 구할 수 있음
    - k = log2(N)
 
### Binary Search Tree (BST)
- 모든 노드들의 키는 서로 다른 유일한 값을 가짐
- 특정 노드 N의 키 값이 N의 왼쪽 서브 트리에 존재하는 모든 노드들의 키 값보다 크고, 오른쪽보다는 작음
- 따라서 BST를 중위 순회(left-root-right)하면서 노드의 키 값을 출력하면, 키 값들이 정렬되어 출력(오름차순)

## Solution
### Recursive Solution
- O(n)
- tree -> list

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def tree_to_list(root) -> list:
            if not root: # 노드가 더이상 존재하지 않을 때
                return []

            return tree_to_list(root.left) + [root.val] + tree_to_list(root.right)
        
        tree_list = tree_to_list(root)
        return tree_list[k-1]
```

### Iterative Solution
- 솔루션을 참고했는데, 처음에 풀이가 직관적으로 와닿지 않았다. (지금도 그럼)
- 한번 더 봐야겠다.
- 일주일 뒤 다시 본 후기 ) 코드를 먼저 이해하려(외우려)하니 잘 이해도 안되고, 습득도 안되었다. 코드를 먼저 보려하지 말고 과정과 순서를 먼저 이해하는 것이 중요하다고 한다. stack에서 pop하는 부분이 헷갈렸는데, 이럴땐 내가 봐야하는 노드의 순서를 먼저 생각해보면 좀 덜 헷갈린다.

```python
'''
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
'''
       
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        
        while cur or stack : # 노드가 더이상 없고 stack이 empty할 때까지
            while cur : # 노드 순회 (left)
                stack.append(cur)
                cur = cur.left # 왼쪽으로 내려가며 stack에 append
                # 전부 순회하고 나면 stack = [15, 10, 8]
                
            cur = stack.pop()
            # cur = 8
            n += 1  # count
            
            if n == k : k번째 pop
                return cur.val
            cur = cur.right # 오른쪽으로 내려가기
```


# 198. House Robber
- Medium

## 의식의 흐름
- dp : i번째까지 최대 money 저장한 리스트
- dp[0] = nums[0]
- dp[1] = nums[1], 전 원소 비교
- 그 외 : dp[n] = dp[n-1], dp[n-2] + nums[n] 중 더 큰 것
- 예외처리를 생각했으나 해당 문제에선 list 길이가 1 이상임이 명시돼있으므로 필요없을듯하다. -> Constraints 잘보기!
- 처음에 dp = [0] 으로 선언해서 영문도 모르고 계속 에러가 났다.

## 관련 개념
### Dynamic Programming
- decide each problem by its sub-problems

## Solution
- Time complexity : O(n)
- Space complexity : O(1)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i==0 :
                dp[0] = nums[0]
            elif i==1 :
                dp[1] = max(dp[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
```


# 느낀점
- 문제 풀 때마다 느끼는 거지만, 풀다 막혀 솔루션을 보면 '이거 아는 개념인데'/'이거 아는 풀이인데!' 하는 경우가 많다.
- 매번 이런 문제가 반복되는 이유를 생각해보았다.
  1. 처음에 개념을 공부할 때, 완벽하게 이해하고 스스로 코드를 작성할 수 있을 때까지 하지 않았다.
  2. 스스로 끝까지 풀어내려는 노력이 부족했다.
- 시간이 없으니 일단 대충 이해하고 넘어가자~가 반복되니 문제가 해결되지 않는듯하다.
- 부족한 만큼 시간을 더 투자해서 아는 개념이더라도 확실하게 정리하고 넘어가야겠다.
- 이번엔 솔루션 앞부분을 먼저 보고 힌트삼아 다시 풀어봤는데, 훨씬 각인이 잘되는것같다. 시간은 많이 걸리지만 당분간은 이 방법을 사용해야겠다.

- 쉽게(깔끔하게) 비교할 수 있는 함수로 max()가 있는데 의외로 잘 생각나지 않더라. 습관화하면 코드도 깔끔해지고 좋을듯
