## 230_Kth Smallest Element in a BST_Tree

- 처음에는 단순하게 그래프를 쭉 탐색하면서 값을 배열에 담은 후, 정렬하여 K번째 요소를 찾는 방식을 취했습니다.

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = defaultdict(int)
        arr = []

        stack = [root]

        while 0 < len(stack):
            node = stack.pop()
            if node.left!=None:
                stack.append(node.left)
            if node.right!=None:
                stack.append(node.right)

            arr.append(node.val)

        arr = sorted(arr)

        return arr[k-1]
```

- 다른 답안을 살펴보다 보니 왜 동작하는 지 의문인 답안들이 있었는데, 정황상 BST는 오른쪽 노드가 무조건 값이 더 크다는 전제가 있는 듯 했습니다. 생각해보니 이름이 '이진 탐색 트리'이기도 하구요.
- 아래의 답안은 이진트리를 우측방향으로 일직선으로 편 후, 완전히 펴졌을 때 가장 작은 노드, 즉, 가장 왼쪽의 노드로부터 K번만큼 오른쪽으로 가서 해당 노드의 값을 반환합니다.

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = 0
        ans = 0
        
        current = root
        
        while current and pos < k:
            
            if not current.left:
                pos += 1
                ans = current.val
                current = current.right
            
            else:
                pre = current.left
                while pre.right:
                    pre = pre.right
                
                pre.right = current
                left = current.left
                current.left = None
                current = left
        
        return ans
```

- 아래 답안은 다소 특이해보이지만, 결론적으로는 BST의 특성을 이용해 재귀적으로 노드를 탐색해들어가면 자연스레 노드의 값들을 정렬하여 반환할 수 있다는 점을 이용한 코드입니다. 거기에 추가로 '제네레이터'라는 개념을 활용했는데, 제가 이해한 바에 따르면 일반적인 반복문은 배열 전체를 메모리에 올려놓고 순회하는 반면 제네레이터는 순회할 차례의 요소만 생성해 메모리에 올리는 식으로 작동해 메모리를 절약할 수 있는 컨셉을 가진 것으로 알고 있습니다.

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for i, num in enumerate(self.helper(root),1):
        if i == k: 
            return num

    def helper(self, root: Optional[TreeNode]) -> Generator:
        if root:
            yield from self.helper(root.left)
            yield root.val
            yield from self.helper(root.right)
```

## 198_House Robber_DP

- 보류...