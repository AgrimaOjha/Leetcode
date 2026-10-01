# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Dummy node to handle edge cases like removing the head node
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # Check if current node is the start of a duplicate sequence
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Bridge over all duplicates
                prev.next = head.next
            else:
                # No duplicate for head.val, advance prev pointer
                prev = prev.next
                
            head = head.next
            
        return dummy.next