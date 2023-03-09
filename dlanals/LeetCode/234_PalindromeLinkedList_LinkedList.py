# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []

        while head != None:
            l.append(head.val)
            tmp = head
            head = head.next

        for idx in range(len(l)//2):
            if l[idx] != l[len(l) - 1 - idx]: return False
        
        return True
        
# Runner
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      rev = None
      slow = fast = head
      
      # runner를 이용해 역순 연결 리스트 구성
      while fast and fast.next:
        fast = fast.next.next # 두 칸 이동
        rev, rev.next, slow = slow, rev, slow.next
      if fast: # 원소 개수가 홀수개일 때
        slow = slow.next
        
      # palindrome 여부 확인
      while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
      return not rev
      
