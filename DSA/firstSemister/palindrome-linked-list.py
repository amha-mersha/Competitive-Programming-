# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        comp = []
        while curr:
            comp.append(curr.val)
            curr = curr.next
        comp = comp[::-1]
        curr = head
        for i in range(len(comp)):
            if comp[i] != curr.val:
                return False
            curr = curr.next
        return True