# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Compute effective rotations needed
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect tail to head to make it circular
        tail.next = head
        
        # 4. Find the new tail: (length - k) steps from head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 5. Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head