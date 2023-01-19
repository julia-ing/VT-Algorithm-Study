# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Divide & Conquer
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
    
    def merge1(self, l, r):
        if not l or not r:
            return l or r
        if l.val< r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r




# Heap
class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # head, curr 노드 생성
        head = ListNode(None)
        curr = head
        
        # 힙 생성
        h = []
        
        # 연결리스트 순회
        for i in range(len(lists)):
            if lists[i]:
            # i번째 연결리스트의 현재 노드와 연결리스트 인덱스를 힙에 push
            # 이 때 heappush(heap, item)
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        # 힙 순회
        while h:
            val, i = heapq.heappop(h)   # 힙으로부터 pop한 것 (최솟값)
            curr.next = ListNode(val)   # curr 노드 이동
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i)) # 힙에 i번째 리스트에서의 노드, 리스트 인덱스 삽입
                lists[i] = lists[i].next # list 이동
        
        return head.next
