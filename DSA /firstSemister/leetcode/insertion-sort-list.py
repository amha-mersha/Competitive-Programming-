# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001,head)
        if not head or not head.next:
            return head
        curr = head.next
        lastsorted = head
        while curr:
            prev = dummy
            if curr.val >= lastsorted.val:
                lastsorted = lastsorted.next
            else:
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastsorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastsorted.next
        return dummy.next 
