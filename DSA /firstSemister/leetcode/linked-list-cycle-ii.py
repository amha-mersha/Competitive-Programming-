# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        curr = head
        while curr:
            if curr not in seen:
                seen.add(curr)
                curr = curr.next
            else:
                return curr
        return 