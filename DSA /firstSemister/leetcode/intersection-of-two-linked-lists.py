# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lghtB = lghtA = 0
        currA, currB = headA, headB
        while currA or currB:
            if currA:
                currA = currA.next
                lghtA += 1
            if currB:
                currB = currB.next
                lghtB += 1
        currA, currB = headA, headB
        if lghtA < lghtB:
            for _ in range(lghtB-lghtA):
                currB = currB.next
        else:
            for _ in range(lghtA - lghtB):
                currA = currA.next
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
