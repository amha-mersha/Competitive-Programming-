# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        curr = head
        dummy = ListNode(None,head)
        start = dummy
        while count != left :
            start = curr
            curr = curr.next
            count += 1
        third = curr
        curr = curr.next
        prev = third
        forward = None
        count += 1
        while count <= right:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            count += 1
        if curr:
            forward = curr.next
        else:
            forward = None
        start.next = prev
        third.next = curr
        return dummy.next
