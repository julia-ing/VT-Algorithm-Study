# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        res = ListNode()
        if len(lists) == 0:
            return

        for linked_list in lists:
            a = linked_list
            while a:
                heappush(heap, a.val)
                a = a.next

        print("->", heap)

        if len(heap) == 0:
            return 

        a = res
        while heap:
            a.val = heappop(heap)
            if heap:
                a.next = ListNode()
            else:
                a.next = None
            a = a.next

        return res
            

        # minheap으로 넣고 pre-ordre로 읽는다. 

        
# 구글링 한 것
# tree search order: preorder, inorder, postorder
# heap 라이브러리
# 궁금한 점: []나 [[]] 처리 어떻게 해주었는지