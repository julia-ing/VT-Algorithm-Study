class Solution:
    def mergeKLists(self, lists):
        result = []
        
        for curr_list in lists:
            while (curr_list != None):
                result.append(curr_list.val)
                curr_list = curr_list.next

        result.sort()

        curr = second = ListNode(0)
        for i in result:
            curr.next = ListNode(i)
            curr = curr.next
        return second.next