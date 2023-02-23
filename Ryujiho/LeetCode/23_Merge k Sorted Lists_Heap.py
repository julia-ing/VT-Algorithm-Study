# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        data = []
        for node in lists:
            if node == None: continue

            while node:
                data.append(node.val)
                node = node.next

        if len(data) == 0: return None
        data.sort()

        answer = ListNode(data[0])
        tmpNode = answer
        for v in range(1, len(data)):
            tmpNode.next = ListNode(data[v])
            tmpNode = tmpNode.next

        return answer