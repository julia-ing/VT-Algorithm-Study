### **Week 3**
|                                  #                                   |        TITLE         |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:--------------------:|:-------------------:|:-------------------------------------:|
| [23](https://leetcode.com/problems/merge-k-sorted-lists/) | Merge k Sorted Lists | Heap                |  <span style="color:red">Hard</span>  |
|      [226](https://leetcode.com/problems/invert-binary-tree/)      |  Invert Binary Tree  |   Tree   | <span style="color:green">Easy</span> |

### 23. Merge k Sorted Lists
#### 문제풀이
-  여러개의 linked list를 sort해줘야하는 문제였다. 보자마자 학부 수업 때 배웠던 내용 같다는 기억에 대충 merge sort 같다는 느낌은 들었는데 구현이 감이 안 와서 그냥 바보 같은 해법을 사용했다.

```
for curr_list in lists:
            while (curr_list != None):
                result.append(curr_list.val)
                curr_list = curr_list.next
result.sort()
```
- 먼저 우리가 반환할 결과에 list를 넣어주고 전체 sort를 해준다. 
```
        curr = return_list = ListNode(0)
        for i in result:
            curr.next = ListNode(i)
            curr = curr.next
        return return_list.next
```
- 그 후 다시 list를 돌며 linked list로 연결을 해준다.
#### 💡 What I learned!
```
def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
```

merge sort를 짚고는 넘어가야 할 것 같아서 풀이를 참고했다. (참고로 해당 코드는 compile이 안됐다. 하지만 로직 참고용!). Divide and conquer로 merge를 다시 불러준다.
또한 희미한 기억으로 c++은 이미 linked list가 기본이나 library로 구현이 되어있었던 것 같은데 queue 등등의 구조를 사용하기에 파이썬이 불편하다는 생각이 들었다.

-------------------------------------------------------------------
### 226. Invert Binary Tree
#### 문제풀이
```
        if not root:
            return
        q = [root]

        while q:
            node = q.pop(0)
```
- root를 가져와주고 다음 tree 탐색을 시작해준다. 이때 여기서 list에서 하나씩 꺼내오므로 bfs를 써준다.

```     
            temp=TreeNode(left=node.left)
            node.left=node.right
            node.right=temp.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
```
- 하나씩 돌면서 inverse를 해준다!

#### 💡 What I learned!
Tree는 항상 봐도 너무 어렵다.. 나는 tree가 제일 싫다..
