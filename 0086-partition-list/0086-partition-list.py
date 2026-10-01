# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # Dummy nodes to anchor the start of both lists
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to track the tail of both lists
        less = less_head
        greater = greater_head
        
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Prevent cycle by severing the tail of the greater list
        greater.next = None
        
        # Connect the less list to the greater list
        less.next = greater_head.next
        
        return less_head.next