# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for node in lists:
            while node:
                nodes.append(ListNode(node.val))
                node = node.next
        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0] if nodes else None