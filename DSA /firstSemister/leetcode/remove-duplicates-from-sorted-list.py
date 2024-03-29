# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        while curr and curr.next:
            nextnode = curr.next
            while nextnode and curr.val == nextnode.val:
                nextnode = nextnode.next
            curr.next = nextnode
            curr = nextnode
        return head