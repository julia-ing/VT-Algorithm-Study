## 1. Merge k Sorted Lists

### 🔮 My solution

- 첫번째 접근은 다음과 같았다. 리스트를 돌면서 아이템이 있을 동안 결과에 append 시켜주고 (merge)
마지막에 머지된 리스트를 간단하게 정렬시켜주는 방식이다.
- 그러나 타입 에러가 발생했다..

```python
def mergeKLists(self, lists):
    res = []
    for list_item in lists:
        root = list_item
        while root:
            res.append(root.val)
            root = root.next
    return sorted(res)
```

에러: `TypeError: [1, 1, 2, 3, 4, 4, 5, 6] is not valid value for the expected return type ListNode`

결과가 단순히 숫자리스트면 안되고, 아이템들이 Node 여야하는 것 같았다.
따라서 위의 코드에서 다음과 같은 코드를 추가했다. 

```python
head = point = ListNode(0)

for x in sorted(res):
    point.next = ListNode(x)
    point = point.next
return head.next
```

이 코드는 정렬된 리스트를 돌아가면서 아이템들을 ListNode 구조로 만들어준다.

해당 접근의 시간복잡도: O(NlogN) 

설명: (리트코드 official 참고)
```text
Collecting all the values costs O(N) time.
A stable sorting algorithm costs O(NlogN) time.
Iterating for creating the linked list costs O(N) time.
```

### 🦦 Optimization (other solutions)

- 이 문제의 난이도가 Hard 라는 게 믿어지지 않기도 했고 tag 가 "Heap" 이었어서 
힙을 사용한 풀이를 고민해보았다.
- 처음에는 `heapq.heappush(heap, (lists[i].val, lists[i]))` 이렇게 자신의 값과 next 만 저장하도록 했는데
에러가 발생했다 : `TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'`
- 찾아보니 lists[i].val 값이 unique 하지 않을 때 두번째 값인 lists[i]로 비교를 하게 되는데, 이 값의 형태가 ListNode여서
크기 비교를 할 수 없다는 에러를 뱉은 것이었다. [참고링크](https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances)
- 따라서 val 값이 같으면 i (유니크한 인덱스) 값으로 비교하게끔 코드를 수정해야 한다.

```python
def mergeKLists(self, lists):
      heap = []
      root = result = ListNode(None)
      # 리스트에 있는 노드들을 힙에 저장
      for i in range(len(lists)):
          if lists[i]:
              heapq.heappush(heap, (lists[i].val, i, lists[i]))

      # pop으로 노드를 빼고, next 로 순회하며 push 
      while heap:
          node = heapq.heappop(heap)
          idx = node[1]
          result.next = node[2]

          result = result.next
          if result.next:
              heapq.heappush(heap, (result.next.val, idx, result.next))

      return root.next
```
처음에 시도했던 코드와 두번째 코드의 런타임은 비슷했다. 그러나 두번째 heap을 사용한 코드가 memory 측면에서 훨씬 좋은 결과를 보였다.

### 👊 문제 회고

문제를 풀며 새로운 에러들을 만났다. 특히 heappush 할 때 났던 비교 관련 에러를 기억해두면
다음에 heap을 활용할 때 많은 도움이 될 것 같다.

## 2. Invert Binary Tree

### 🔮 My solution

- 쉽게 생각할 수 있는 재귀를 사용했다.
- 시간복잡도 O(N) : 트리 노드들이 한번씩만 방문되므로

```python
def invertTree(self, root):
    if root is None:
        return root
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```

### 🦦 other solutions

- 재귀를 queue 로 대신한 풀이이다.
- 시간복잡도는 같다.

```python
def invertTree(self, root):
    if not root:
        return None
    
    queue = collections.deque([root])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
    
    return root
```

### 👊 문제 회고

easy 문제여도 풀이가 하나는 아니다! 재귀가 떠올리기에는 쉽지만, 다른 대안 풀이를 생각해보는 것도 연습해봐야겠다.. 
