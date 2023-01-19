from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hash_table = defaultdict(int)

        for list_node in lists:
            node = list_node
            while node:
                hash_table[node.val]+=1
                node = node.next

        if not hash_table:
            return
        
        key_list = sorted(hash_table.keys())

        root_node = last_node = cur_node = ListNode()
        for key in key_list:
            for _ in range(hash_table[key]):
                cur_node.val = key
                cur_node.next = ListNode()
                last_node = cur_node
                cur_node = cur_node.next
        
        last_node.next = None

        return root_node