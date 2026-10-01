"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root  # Pointer to traverse the current level
        
        while curr:
            dummy = Node(0)  # Dummy head for the next level
            tail = dummy     # Tail pointer to build the next level's linked list
            
            # Iterate through all nodes in the current level via 'next' pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            # Move to the start of the next level
            curr = dummy.next
            
        return root
        