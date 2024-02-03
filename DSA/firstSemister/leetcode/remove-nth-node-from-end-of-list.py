# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lght = 1
        curr = head
        while curr and curr.next:
            curr = curr.next
            lght += 1
        lght -= n
        if lght == 0:
            head = head.next
            return head 
        curr = head
        count = 1
        while curr and curr.next:
            if count == lght:
                curr.next = curr.next.next
                return head
            curr = curr.next
            count += 1
        
