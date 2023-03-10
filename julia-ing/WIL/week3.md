## 1. Merge k Sorted Lists

### ๐ฎ My solution

- ์ฒซ๋ฒ์งธ ์ ๊ทผ์ ๋ค์๊ณผ ๊ฐ์๋ค. ๋ฆฌ์คํธ๋ฅผ ๋๋ฉด์ ์์ดํ์ด ์์ ๋์ ๊ฒฐ๊ณผ์ append ์์ผ์ฃผ๊ณ  (merge)
๋ง์ง๋ง์ ๋จธ์ง๋ ๋ฆฌ์คํธ๋ฅผ ๊ฐ๋จํ๊ฒ ์ ๋ ฌ์์ผ์ฃผ๋ ๋ฐฉ์์ด๋ค.
- ๊ทธ๋ฌ๋ ํ์ ์๋ฌ๊ฐ ๋ฐ์ํ๋ค..

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

์๋ฌ: `TypeError: [1, 1, 2, 3, 4, 4, 5, 6] is not valid value for the expected return type ListNode`

๊ฒฐ๊ณผ๊ฐ ๋จ์ํ ์ซ์๋ฆฌ์คํธ๋ฉด ์๋๊ณ , ์์ดํ๋ค์ด Node ์ฌ์ผํ๋ ๊ฒ ๊ฐ์๋ค.
๋ฐ๋ผ์ ์์ ์ฝ๋์์ ๋ค์๊ณผ ๊ฐ์ ์ฝ๋๋ฅผ ์ถ๊ฐํ๋ค. 

```python
head = point = ListNode(0)

for x in sorted(res):
    point.next = ListNode(x)
    point = point.next
return head.next
```

์ด ์ฝ๋๋ ์ ๋ ฌ๋ ๋ฆฌ์คํธ๋ฅผ ๋์๊ฐ๋ฉด์ ์์ดํ๋ค์ ListNode ๊ตฌ์กฐ๋ก ๋ง๋ค์ด์ค๋ค.

ํด๋น ์ ๊ทผ์ ์๊ฐ๋ณต์ก๋: O(NlogN) 

์ค๋ช: (๋ฆฌํธ์ฝ๋ official ์ฐธ๊ณ )
```text
Collecting all the values costs O(N) time.
A stable sorting algorithm costs O(NlogN) time.
Iterating for creating the linked list costs O(N) time.
```

### ๐ฆฆ Optimization (other solutions)

- ์ด ๋ฌธ์ ์ ๋์ด๋๊ฐ Hard ๋ผ๋ ๊ฒ ๋ฏฟ์ด์ง์ง ์๊ธฐ๋ ํ๊ณ  tag ๊ฐ "Heap" ์ด์์ด์ 
ํ์ ์ฌ์ฉํ ํ์ด๋ฅผ ๊ณ ๋ฏผํด๋ณด์๋ค.
- ์ฒ์์๋ `heapq.heappush(heap, (lists[i].val, lists[i]))` ์ด๋ ๊ฒ ์์ ์ ๊ฐ๊ณผ next ๋ง ์ ์ฅํ๋๋ก ํ๋๋ฐ
์๋ฌ๊ฐ ๋ฐ์ํ๋ค : `TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'`
- ์ฐพ์๋ณด๋ lists[i].val ๊ฐ์ด unique ํ์ง ์์ ๋ ๋๋ฒ์งธ ๊ฐ์ธ lists[i]๋ก ๋น๊ต๋ฅผ ํ๊ฒ ๋๋๋ฐ, ์ด ๊ฐ์ ํํ๊ฐ ListNode์ฌ์
ํฌ๊ธฐ ๋น๊ต๋ฅผ ํ  ์ ์๋ค๋ ์๋ฌ๋ฅผ ๋ฑ์ ๊ฒ์ด์๋ค. [์ฐธ๊ณ ๋งํฌ](https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances)
- ๋ฐ๋ผ์ val ๊ฐ์ด ๊ฐ์ผ๋ฉด i (์ ๋ํฌํ ์ธ๋ฑ์ค) ๊ฐ์ผ๋ก ๋น๊ตํ๊ฒ๋ ์ฝ๋๋ฅผ ์์ ํด์ผ ํ๋ค.

```python
def mergeKLists(self, lists):
      heap = []
      root = result = ListNode(None)
      # ๋ฆฌ์คํธ์ ์๋ ๋ธ๋๋ค์ ํ์ ์ ์ฅ
      for i in range(len(lists)):
          if lists[i]:
              heapq.heappush(heap, (lists[i].val, i, lists[i]))

      # pop์ผ๋ก ๋ธ๋๋ฅผ ๋นผ๊ณ , next ๋ก ์ํํ๋ฉฐ push 
      while heap:
          node = heapq.heappop(heap)
          idx = node[1]
          result.next = node[2]

          result = result.next
          if result.next:
              heapq.heappush(heap, (result.next.val, idx, result.next))

      return root.next
```
์ฒ์์ ์๋ํ๋ ์ฝ๋์ ๋๋ฒ์งธ ์ฝ๋์ ๋ฐํ์์ ๋น์ทํ๋ค. ๊ทธ๋ฌ๋ ๋๋ฒ์งธ heap์ ์ฌ์ฉํ ์ฝ๋๊ฐ memory ์ธก๋ฉด์์ ํจ์ฌ ์ข์ ๊ฒฐ๊ณผ๋ฅผ ๋ณด์๋ค.

### ๐ ๋ฌธ์  ํ๊ณ 

๋ฌธ์ ๋ฅผ ํ๋ฉฐ ์๋ก์ด ์๋ฌ๋ค์ ๋ง๋ฌ๋ค. ํนํ heappush ํ  ๋ ๋ฌ๋ ๋น๊ต ๊ด๋ จ ์๋ฌ๋ฅผ ๊ธฐ์ตํด๋๋ฉด
๋ค์์ heap์ ํ์ฉํ  ๋ ๋ง์ ๋์์ด ๋  ๊ฒ ๊ฐ๋ค.

## 2. Invert Binary Tree

### ๐ฎ My solution

- ์ฝ๊ฒ ์๊ฐํ  ์ ์๋ ์ฌ๊ท๋ฅผ ์ฌ์ฉํ๋ค.
- ์๊ฐ๋ณต์ก๋ O(N) : ํธ๋ฆฌ ๋ธ๋๋ค์ด ํ๋ฒ์ฉ๋ง ๋ฐฉ๋ฌธ๋๋ฏ๋ก

```python
def invertTree(self, root):
    if root is None:
        return root
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```

### ๐ฆฆ other solutions

- ์ฌ๊ท๋ฅผ queue ๋ก ๋์ ํ ํ์ด์ด๋ค.
- ์๊ฐ๋ณต์ก๋๋ ๊ฐ๋ค.

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

### ๐ ๋ฌธ์  ํ๊ณ 

easy ๋ฌธ์ ์ฌ๋ ํ์ด๊ฐ ํ๋๋ ์๋๋ค! ์ฌ๊ท๊ฐ ๋ ์ฌ๋ฆฌ๊ธฐ์๋ ์ฝ์ง๋ง, ๋ค๋ฅธ ๋์ ํ์ด๋ฅผ ์๊ฐํด๋ณด๋ ๊ฒ๋ ์ฐ์ตํด๋ด์ผ๊ฒ ๋ค.. 
