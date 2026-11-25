from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 1: Count total nodes in the linked list
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next

        curr = head

        # Step 2: Construct BST in inorder fashion using `count` nodes
        def build(count: int) -> Optional[TreeNode]:
            nonlocal curr
            if count <= 0:
                return None

            left = build(count // 2)

            root = TreeNode(curr.val)
            curr = curr.next

            root.left = left
            root.right = build(count - (count // 2) - 1)
            return root

        return build(length)