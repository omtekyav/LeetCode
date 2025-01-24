# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # If empty list or single node, return as is
            return head
        
        left_node = None
        middle_node = head

        while middle_node is not None:
            right_node = middle_node.next  # Save next node
            middle_node.next = left_node   # Reverse pointer
            left_node = middle_node        # Move left_node forward
            middle_node = right_node       # Move middle_node forward

        return left_node  # New head of reversed list
