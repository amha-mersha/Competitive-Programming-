# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curr = node
        while curr:
            next_node = curr.next
            if next_node.next == None:
                curr.val = next_node.val
                curr.next = None
                return
            curr.val = next_node.val
            curr = curr.next
