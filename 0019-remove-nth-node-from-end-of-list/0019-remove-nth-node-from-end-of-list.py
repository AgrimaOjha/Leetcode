# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Advance fast pointer so that the distance between fast and slow is n + 1 nodes
        for _ in range(n + 1):
            fast = fast.next
            
        # Move fast to the end, maintaining the gap
        while fast:
            fast = fast.next
            slow = slow.next
            
        # Skip the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next